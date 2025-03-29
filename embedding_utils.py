from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Initialize the model
model = SentenceTransformer("all-MiniLM-L6-v2")
print(f"Model initialized: {model}")

# Initialize FAISS index
index = faiss.IndexFlatL2(384)  # Embedding size for "all-MiniLM-L6-v2"

# Function for embedding descriptions
def build_index(descriptions):
    embeddings = model.encode([desc["description"] for desc in descriptions])
    index.add(np.array(embeddings, dtype="float32"))
    return embeddings

# Find the closest match for a query
def find_closest_function(query):
    query_vector = model.encode([query])[0].reshape(1, -1)
    distances, indices = index.search(np.array(query_vector, dtype="float32"), 1)
    return indices[0][0], distances[0][0]  # Return index and distance
