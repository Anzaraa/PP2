import os

def check_path(path):
    """Checks if a given path exists and extracts filename and directory."""
    
    if os.path.exists(path):  # Check if path exists
        print(f" The path exists: {path}")
        
        # Get the directory and filename
        directory = os.path.dirname(path)
        filename = os.path.basename(path)
        
        print(f" Directory: {directory}")
        print(f" Filename: {filename}")
    
    else:
        print(f" The path does not exist: {path}")

# Example: Replace with your actual path
path_to_check = r"C:\Users\Huawei\Desktop\Lecture\Labs\Lab6\dir-and-files\test.txt"
check_path(path_to_check)
