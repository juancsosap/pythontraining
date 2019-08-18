import os

# Get Current Working Directory (CWD)
cwd1 = os.getcwd()
print(cwd1)

# Change CWD
# Relative Path
os.chdir('..')
cwd2 = os.getcwd()
print(cwd2)

# Absolute Path
os.chdir('/tmp')
cwd3 = os.getcwd()
print(cwd3)

print()

# List Directory

# List CWD
os.chdir(cwd1)
cwd = os.getcwd()
print(cwd)
dir_list = os.listdir()
print(dir_list)

# List Path
dir_list = os.listdir('..')
print(dir_list)

print()

# Create Directory
os.mkdir('newdocs')
dir_list = os.listdir()
print(dir_list)

print()

# Rename file or directory
os.rename('newdocs','olddocs')
dir_list = os.listdir()
print(dir_list)

print()

# Removing file
dir_list = os.listdir('docs')
print(dir_list)
os.remove('docs/doc-copy.txt')
dir_list = os.listdir('docs')
print(dir_list)

print()

# Removing directory
dir_list = os.listdir()
print(dir_list)
os.rmdir('olddocs')
dir_list = os.listdir()
print(dir_list)
