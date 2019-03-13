#   STACK   |   HEAP
# -----------------------
#           |
#   var11   |   A1A1
#   ------  |  --------
#  | A1A1 | | | 'HOLA' |
#   ------  |  --------
#           |

# The STACK memory store the reference to the HEAP memory
# address where the value is stored
var11 = 'HOLA'
print(var11)

#   STACK   |   HEAP
# -----------------------
#           |
#   var11   |   ABAB
#   ------  |  --------
#  | ABAB | | | 'CHAO' |
#   ------  |  --------
#           |

# When the value is modified a new object in the HEAP memory
# is created and the STACK memory store the reference to new
# HEAP memory address where the value is stored
var11 = 'CHAO'
print(var11)

#   STACK   |   HEAP
# -----------------------
#           |
#   var11   |   ABAB
#   ------  |  --------
#  | ABAB | | | 'CHAO' |
#   ------  |  --------
#           |
#   var12   |
#   ------  |
#  | ABAB | |
#   ------  |
#           |

# When the second variable is assigned with the first
# variable value, it store the same reference to the HEAP
# address memory where the value is stored
var12 = var11
print(var11, var12)

#   STACK   |   HEAP
# -----------------------
#           |
#   var11   |   ABAB
#   ------  |  --------
#  | ABAB | | | 'CHAO' |
#   ------  |  --------
#           |
#   var12   |   ACAC
#   ------  |  --------
#  | ACAC | | | 'YEAH' |
#   ------  |  --------
#           |

# When the value of one variable is modified with a new
# value, the reference address is change to the HEAP memory
# address where is stored the new object value, and the
# other variable remains with the reference to the original
# value
var12 = 'YEAH'
print(var11, var12)
