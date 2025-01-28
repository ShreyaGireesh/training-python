import filecmp

# Compare two directories
dir1 = 'dir1'
dir2 = 'dir2'

# Create a dircmp object for the directories
dcmp = filecmp.dircmp(dir1, dir2)

# Print a comparison report
print("Report:")
dcmp.report()

# Print a partial comparison report (just immediate subdirectories and files)
print("\nPartial Comparison Report (report_partial_closure):")
dcmp.report_partial_closure() 

# Print a full comparison report (recursive, all subdirectories)
print("\nFull Recursive Comparison Report (report_full_closure):")
dcmp.report_full_closure()  

# Print files that are only in directory 1
print("\nFiles only in directory 1:")
print(dcmp.left_only)

# Print files that are only in directory 2
print("\nFiles only in directory 2:")
print(dcmp.right_only)

# Print common files and directories in both directories
print("\nCommon files and directories:")
print(dcmp.common)

# Print files with differing contents
print("\nFiles with differences:")
print(dcmp.diff_files)

# Print files that are identical in both dir1 and dir2
print("\nFiles that are the same in both directories (same_files):")
print(dcmp.same_files)

# Print common files (files that are in both directories, regardless of subdirectories)
print("\nCommon files (all directories):")
print(dcmp.common_files)
