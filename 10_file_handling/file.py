"""
10 - File Handling
------------------
Reading from and writing to files using Python's built-in open().
"""

import os
import json

# Use a path relative to this script so the demo works from any directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SAMPLE_FILE = os.path.join(BASE_DIR, "sample.txt")
JSON_FILE = os.path.join(BASE_DIR, "data.json")

# --- Writing to a file ('w' overwrites existing content) ---
with open(SAMPLE_FILE, "w") as f:
    f.write("Hello, this is line 1.\n")
    f.write("This is line 2.\n")

# --- Appending to a file ('a' adds to the end) ---
with open(SAMPLE_FILE, "a") as f:
    f.write("This is an appended line.\n")

# --- Reading the entire file ---
with open(SAMPLE_FILE, "r") as f:
    content = f.read()
print("--- Full content ---")
print(content)

# --- Reading line by line ---
with open(SAMPLE_FILE, "r") as f:
    print("--- Line by line ---")
    for line in f:
        print(line.strip())   # strip() removes the trailing newline

# --- Reading all lines into a list ---
with open(SAMPLE_FILE, "r") as f:
    lines = f.readlines()
print("--- As a list ---")
print(lines)

# --- Why use 'with'? ---
# It automatically closes the file for you, even if an error occurs.
# Without 'with', you'd need to manually call f.close().

# --- Checking if a file exists ---
print("File exists:", os.path.exists(SAMPLE_FILE))

# --- Working with JSON files ---
data = {
    "name": "Hamza",
    "age": 24,
    "skills": ["Python", "Node.js", "SQL"]
}

with open(JSON_FILE, "w") as f:
    json.dump(data, f, indent=4)

with open(JSON_FILE, "r") as f:
    loaded_data = json.load(f)
print("--- Loaded JSON ---")
print(loaded_data)
print("Name from JSON:", loaded_data["name"])

# --- Reading file safely with error handling ---
try:
    with open(os.path.join(BASE_DIR, "does_not_exist.txt"), "r") as f:
        f.read()
except FileNotFoundError:
    print("File not found! Handled gracefully.")

# --- Cleanup (optional) ---
# Uncomment to remove the demo files after running
# os.remove(SAMPLE_FILE)
# os.remove(JSON_FILE)
