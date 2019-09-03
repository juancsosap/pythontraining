basedir = __file__[:__file__.rfind('/')+1]

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
os.chdir(basedir)
cwd3 = os.getcwd()
print(cwd3)

print()

# List Directory

# List CWD
dir_list = os.listdir()
print(dir_list)

print()

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
os.rename('newdocs', 'olddocs')
dir_list = os.listdir()
print(dir_list)

print()

# Creating File
open('docs/other.txt', 'w').close()
dir_list = os.listdir('docs')
print(dir_list)

print()

# Removing file
os.remove('docs/other.txt')
dir_list = os.listdir('docs')
print(dir_list)

print()

# Removing directory
dir_list = os.listdir()
print(dir_list)
os.rmdir('olddocs')
dir_list = os.listdir()
print(dir_list)
