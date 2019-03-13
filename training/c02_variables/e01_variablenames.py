# The variables name could not begin with number
# 1num = 1

# The variable name is case sencitive (Upper and Lower case are different)
num1 = 10
NUM1 = 10
Num1 = 10

# The variables names could have uppercase and lowercase letters, numbers and
# underscore (_) symbols
myNum_1 = 20

# The variable name must be short but clear
thisismyverylongvariablename = 10 # Not recommended - Too Long
a = 10 # Not recommended - Too short
name = "John" # Recommended - Clear and Short

# There are many convention to define the variable names
first_number = 20 # Underscore word separation
secondNumber = 30 # Cammel Case word separation

# Some word could be used as variable names, but are not recommended because
# are associated to a predefined classes
int = 20 # valid, but not recommended, built in class
complex = 20 # valid, but not recommended, built in class

# Some words can't be used as variables names, because are python language keywords
# for = 30 # invalid, reserved keyword

# The variable definition and initialization could be did one or many at the time
n0 = 10
n1, n2, n3 = 10, 20, 30
