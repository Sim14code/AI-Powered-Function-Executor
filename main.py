from fastapi import FastAPI, HTTPException
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from function_store import *

# Initialize FastAPI app
app = FastAPI()

# Initialize FAISS index and SentenceTransformer model
index = faiss.IndexFlatL2(384)  # Embedding size for "all-MiniLM-L6-v2"
model = SentenceTransformer("all-MiniLM-L6-v2")  # Initialize the model



# Build the FAISS index
def build_index(descriptions):
    embeddings = model.encode([desc["description"] for desc in descriptions])
    index.add(np.array(embeddings, dtype="float32"))
    print(f"FAISS index built with {len(descriptions)} descriptions.")
    return embeddings

# Initialize the index with function descriptions
build_index(function_descriptions)

# Route to execute a function based on a query
from pydantic import BaseModel

class QueryRequest(BaseModel):
    query: str

@app.post("/execute")
def execute_function(request: QueryRequest):
    """
    Endpoint to execute a function based on the query.
    Args:
        request (QueryRequest): The request body containing the query string.
    Returns:
        dict: Name and result of the executed function.
    """
    query = request.query
    try:
        # Find the closest matching function
        query_vector = model.encode([query])[0].reshape(1, -1)
        distances, indices = index.search(np.array(query_vector, dtype="float32"), 1)
        function_index, distance = indices[0][0], distances[0][0]

        if distance > 0.5:
            raise HTTPException(status_code=404, detail="No matching function found.")
        
        if function_index < 0 or function_index >= len(function_descriptions):
            raise HTTPException(status_code=500, detail="Invalid function index.")
        
        function_name = function_descriptions[function_index]["name"]
        print(f"Function Name: {function_name}")
        
        if function_name not in functions:
            raise HTTPException(status_code=404, detail=f"Function '{function_name}' not found.")
        
        # Execute the matched function
        try:
            result = functions[function_name]()
            print(f"Function Result: {result}")
            return {"function": function_name, "result": result}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error executing function: {e}")
    
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error.")
