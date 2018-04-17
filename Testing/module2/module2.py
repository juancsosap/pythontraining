import sys
import os
BASEDIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append('{}/..'.format(BASEDIR))


import module1.module1

print('From MODULE2.MODULE2')
