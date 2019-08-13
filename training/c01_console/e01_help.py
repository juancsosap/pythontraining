# Shows the resources (Variables, Classes, Libraries) available in the session
# The resources within double under-scores (__XXXXX__) are internal of the system
print(dir()) # print something

# Shows the libraries imported by the session
print(dir(__builtins__))

# Shows the methods and fields availables in one class
print(dir(str))

# Shows the help about the use and parameters of the method
help(print) # Q key to exit

# The application mantain in the session all the resources required to operate
# including the reference to variables, methods, classes, ... that interact with
# the operative system and the Hardware
# APPLICATION --> SESSION --> LIBRARIES --> OS --> HW
