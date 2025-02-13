import os

# Get the current working directory
current_directory = os.getcwd()
print(f"Current Directory: {current_directory}")

# Join paths using os.path.join() (creating a new file path)
file_name = "strings.py"
file_path = os.path.join(current_directory, file_name)
print(f"\nJoined file path: {file_path}")

# Check if the file exists using os.path.exists()
if os.path.exists(file_path):
    print(f"\nThe file {file_name} exists!")
else:
    print(f"\nThe file {file_name} does not exist.")

# Get the absolute path of the file using os.path.abspath()
absolute_path = os.path.abspath(file_name)
print(f"\nAbsolute path of {file_name}: {absolute_path}")

# Get the file extension using os.path.splitext()
file_name, file_extension = os.path.splitext(file_name)
print(f"\nFile name: {file_name}, File extension: {file_extension}")

# Check if the path is a directory or file using os.path.isdir() and os.path.isfile()
print(f"\nIs the path a directory? {os.path.isdir(file_path)}")
print(f"Is the path a file? {os.path.isfile(file_path)}")

# Get the directory name of the file path using os.path.dirname()
directory_name = os.path.dirname(file_path)
print(f"\nDirectory name of the file path: {directory_name}")

# Get the base name (file name) using os.path.basename()
base_name = os.path.basename(file_path)
print(f"\nBase name (file name) of the path: {base_name}")
