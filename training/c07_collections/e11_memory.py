#   STACK   |   HEAP
#           |
#   var21   |   1234          ABA1      ABA2      ABA3
#   ------  |  ------        ------    ------    ------
#  | 1234 | | | ABA1 | 0    |  12  |  |  34  |  |  56  |
#   ------  |  ------        ------    ------    ------
#           | | ABA2 | 1
#           |  ------
#           | | ABA3 | 2
#           |  ------
#           |

# The STACK memory store the reference to the HEAP memory
# address where the array object is stored, it is used to
# mantain the object structure. Each index has a reference
# to the HEAP memory address where each value object of the
# array is stored
var21 = [12, 34, 56]
print(var21)

#   STACK   |   HEAP
#           |
#   var21   |   1234          ABA1      ABA2      ABA4
#   ------  |  ------        ------    ------    ------
#  | 1234 | | | ABA1 | 0    |  12  |  |  34  |  |  78  |
#   ------  |  ------        ------    ------    ------
#           | | ABA2 | 1
#           |  ------
#           | | ABA4 | 2
#           |  ------
#           |

# When one element of the array is modified, only the
# reference of that element is modified
var21[2] = 78
print(var21)

#   STACK   |   HEAP
#           |
#   var21   |   1234          ABA1      ABA2      ABA4
#   ------  |  ------        ------    ------    ------
#  | 1234 | | | ABA1 | 0    |  12  |  |  34  |  |  78  |
#   ------  |  ------        ------    ------    ------
#           | | ABA2 | 1
#   var22   |  ------
#   ------  | | ABA4 | 2
#  | 1234 | |  ------
#   ------  |
#           |

# When the second variable is assigned with the first
# variable value, it store the same reference to the HEAP
# address memory where the value is stored
var22 = var21
print(var21, var22)

#   STACK   |   HEAP
#           |
#   var21   |   1234          ABA1      ABA5      ABA4
#   ------  |  ------        ------    ------    ------
#  | 1234 | | | ABA1 | 0    |  12  |  |  90  |  |  78  |
#   ------  |  ------        ------    ------    ------
#           | | ABA5 | 1
#   var22   |  ------
#   ------  | | ABA4 | 2
#  | 1234 | |  ------
#   ------  |
#           |

# When one element of the array is modified, only the
# reference of that element is modified, but as both
# variables point to the same object, both are affected
var22[1] = 90
print(var21, var22)

#   STACK   |   HEAP
#           |
#   var21   |   1234          ABA1      ABA5      ABA4
#   ------  |  ------        ------    ------    ------
#  | 1234 | | | ABA1 | 0    |  12  |  |  90  |  |  78  |
#   ------  |  ------        ------    ------    ------
#           | | ABA5 | 1
#   var22   |  ------
#   ------  | | ABA4 | 2
#  | 1234 | |  ------
#   ------  |
#           |
#   var23   |   5678
#   ------  |  ------
#  | 5678 | | | ABA1 | 0
#   ------  |  ------
#           | | ABA5 | 1
#           |  ------
#           | | ABA4 | 2
#           |  ------
#           |

# When one variable is created as a copy of the other variable
# a new object in the HEAP memory is created as a copy of the
# other object, but the reference to neted levels remain equals
var23 = var21.copy()
print(var21, var22, var23)

#   STACK   |   HEAP
#           |
#   var21   |   1234          ABA1      ABA5      ABA4
#   ------  |  ------        ------    ------    ------
#  | 1234 | | | ABA1 | 0    |  12  |  |  90  |  |  78  |
#   ------  |  ------        ------    ------    ------
#           | | ABA5 | 1
#   var22   |  ------
#   ------  | | ABA4 | 2
#  | 1234 | |  ------
#   ------  |
#           |
#   var23   |   5678          ABA6
#   ------  |  ------        ------
#  | 5678 | | | ABA1 | 0    |  13  |
#   ------  |  ------        ------
#           | | ABA6 | 1
#           |  ------
#           | | ABA4 | 2
#           |  ------
#           |

# When one element of the array is modified in the copy object,
# the other arrays are no affected
var23[1] = 13
print(var21, var22, var23)

#   STACK   |   HEAP
#           |
#   var24   |   A123          B123      B456
#   ------  |  ------        ------    ------
#  | A123 | | | B123 | 0    | C001 |  | C003 |
#   ------  |  ------        ------    ------
#           | | B456 | 1    | C002 |  | C004 |
#           |  ------        ------    ------
#           |
#           |   C001      C002      C003      C004
#           |  ------    ------    ------    ------
#           | |  11  |  |  12  |  |  21  |  |  22  |
#           |  ------    ------    ------    ------
#           |

# When multidimentional arrays are created multple nested
# object are created in the HEAP memory
var24 = [[11,12],[21,22]]
print(var24)

#   STACK   |   HEAP
#           |
#   var24   |   A123          B123      B456
#   ------  |  ------        ------    ------
#  | A123 | | | B123 | 0    | C001 |  | C003 |
#   ------  |  ------        ------    ------
#           | | B456 | 1    | C002 |  | C004 |
#           |  ------        ------    ------
#           |
#           |   C001      C002      C003      C004
#           |  ------    ------    ------    ------
#           | |  11  |  |  12  |  |  21  |  |  22  |
#           |  ------    ------    ------    ------
#           |
#   var24   |   A789
#   ------  |  ------
#  | A789 | | | B123 | 0
#   ------  |  ------
#           | | B456 | 1
#           |  ------
#           |

# When copy array object is created a new object is
# created in the HEAP memory copying the values in the
# original object. Then, the reference to the neted objects
# remain the same
var25 = var24.copy()
print(var24, var25)

#   STACK   |   HEAP
#           |
#   var24   |   A123          B123      B456
#   ------  |  ------        ------    ------
#  | A123 | | | B123 | 0    | C005 |  | C003 |
#   ------  |  ------        ------    ------
#           | | B456 | 1    | C002 |  | C004 |
#           |  ------        ------    ------
#           |
#           |   C005      C002      C003      C004
#           |  ------    ------    ------    ------
#           | |  34  |  |  12  |  |  21  |  |  22  |
#           |  ------    ------    ------    ------
#           |
#   var24   |   A789
#   ------  |  ------
#  | A789 | | | B123 | 0
#   ------  |  ------
#           | | B456 | 1
#           |  ------
#           |

# If a modification in a neted object is made, both arrays
# are affected
var25[0][0] = 34
print(var24, var25)
