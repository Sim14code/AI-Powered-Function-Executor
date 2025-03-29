import subprocess
import psutil  # For CPU usage (install with `pip install psutil`)

# Define functions with actual implementations
functions = {
    "open_calculator": lambda: subprocess.Popen("calc.exe", shell=True),  # Opens calculator
    "get_cpu_usage": lambda: f"Current CPU usage: {psutil.cpu_percent()}%",  # Retrieves CPU usage
    "shutdown_system": lambda: subprocess.run("shutdown /s /t 1", shell=True),  # Shuts down the system
}

# Function descriptions for FAISS indexing
function_descriptions = [
    {"name": "open_calculator", "description": "Opens the calculator application."},
    {"name": "get_cpu_usage", "description": "Retrieves the current CPU usage."},
    {"name": "shutdown_system", "description": "Shuts down the system."},
]
