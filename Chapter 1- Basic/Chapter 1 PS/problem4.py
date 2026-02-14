import os

directory_path = r"C:\Users\gupta\OneDrive\Documents\PythonProgram\Chapter 2 variables"   # or "C:\\Users\\Dell\\Desktop\\Chapter 1"
try:
    for name in os.listdir(directory_path):
        print(name)
except Exception as e:
    print("Error:", e)
