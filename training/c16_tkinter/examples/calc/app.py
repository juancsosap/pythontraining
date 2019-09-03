import os

basedir = __file__[:__file__.rfind('/')+1]
if basedir != '': os.chdir(basedir)

from view import CalculatorView as Calculator

if __name__ == "__main__":
    Calculator()