# Import all module
import printer as pr
import math

pr.show('from app')
print('pi:', math.pi)

# Import method from module
from printer import call
from math import e

call('from app')
print('e:', e)

# Import all methods from module
from printer import *
from math import *

view('from app')
print('tau:', tau)
