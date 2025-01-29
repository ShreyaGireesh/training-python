from pathlib import Path
import shutil
import tempfile
import filecmp
import time

# Create a file and write some text to it
file_path = Path("old_name.txt")
file_path.write_text("This is some content.")
print(f"File created: {file_path}")
time.sleep(1)

# Rename the file
new_file_path = Path("new_name.txt")
file_path.rename(new_file_path)

# Check if the content is still the same
content = new_file_path.read_text()
print(f"Content of the renamed file: {content}")
time.sleep(1)

# Create a directory
dir_path = Path("example_dir")
dir_path.mkdir(exist_ok=True)  # exist_ok=True prevents error if directory already exists
print(f"Directory created: {dir_path}")
time.sleep(1)

# Create a file inside the directory
new_file_in_dir = dir_path / "nested_example.txt"
new_file_in_dir.touch()
print(f"File created in directory: {new_file_in_dir}")
time.sleep(1)

# Copy and Move Files using shutil
shutil.copy(new_file_path, "copied_example.txt")
shutil.move("copied_example.txt", "moved_example.txt")

# Check if file exists and is a file
if new_file_path.is_file():
    print(f"{new_file_path} is a file.")

# Get file stats
stats = new_file_path.stat()
print(f"File Size: {stats.st_size} bytes")

# Check if files are identical
if filecmp.cmp('new_name.txt', 'moved_example.txt'):
    print("The files are identical.")
else:
    print("The files are different.")

# Create a temporary file
with tempfile.NamedTemporaryFile(delete=False) as temp_file:
    print(f"Temporary file created: {temp_file.name}")
time.sleep(1)

# Delete the file inside the directory
new_file_in_dir.unlink()
print(f"File deleted: {new_file_in_dir}")
time.sleep(1)

# Delete the renamed file
new_file_path.unlink()
print(f"Renamed file deleted: {new_file_path}")
time.sleep(1)



# Remove the directory
dir_path.rmdir()  # This only works if the directory is empty
print(f"Directory removed: {dir_path}")