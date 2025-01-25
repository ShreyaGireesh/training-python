from pathlib import PurePath

# Create a PurePath object
p = PurePath('folder/subfolder/file.txt')
print(f"Original Path: {p}")

# Accessing individual parts of the path
print(f"Parts of the path: {p.parts}")  

# Accessing the file name (last part of the path)
print(f"File name (last part): {p.name}")  

# Accessing the file name without the extension
print(f"File name without extension: {p.stem}")  

# Accessing the file extension
print(f"File extension: {p.suffix}")  

# Accessing the parent directory
print(f"Parent directory: {p.parent}")  

# Joining paths with the / operator
p2 = p / 'anotherfile.txt'  
print(f"Joined path: {p2}")  

# Using the joinpath method to join paths
p3 = p.joinpath('anotherfolder', 'anotherfile.txt')
print(f"Joined path with joinpath: {p3}")  

# Check if the path is absolute (starts from the root directory)
print(f"Is path absolute? {p.is_absolute()}") 

# Changing the file name with with_name
p4 = p.with_name('newfile.txt')
print(f"New path with changed file name: {p4}")  

# Changing the file extension with with_suffix
p5 = p.with_suffix('.md')
print(f"New path with changed extension: {p5}")  

# Making the path relative to another base path
p6 = p.relative_to('folder')
print(f"Relative path: {p6}")  
