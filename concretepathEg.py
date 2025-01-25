from pathlib import Path

# Create a Concrete Path object for a directory
directory = Path('example_folder/subfolder')

# Create directories (if they don't exist)
directory.mkdir(parents=True, exist_ok=True)
print(f"Created directory: {directory}")

# Create a file path inside that directory
file_path = directory / 'example_file.txt'

# Create a new file and write some content into it
file_path.write_text("Hello, this is a test file.")
print(f"File created: {file_path}")

# Read the content from the file
content = file_path.read_text()
print(f"Content of the file: {content}")

# check if the file exists
if file_path.exists():
    print(f"The file {file_path} exists.")

# Get the file's parent directory
parent_directory = file_path.parent
print(f"Parent directory of the file: {parent_directory}")

# Rename the file
renamed_file = file_path.with_name('renamed_file.txt')
file_path.rename(renamed_file)
print(f"File renamed to: {renamed_file}")

# Delete the file
renamed_file.unlink()
print(f"File deleted: {renamed_file}")

# 1Delete the directory (if it's empty)
parent_directory.rmdir()
print(f"Directory deleted: {parent_directory}")
