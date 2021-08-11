import os

class ToolUtils:
    # move de current working directory to the
    # proyect directory 
    @staticmethod
    def locatize():
        if '__file__' in dir(__builtins__):
            basedir = os.path.dirname(__file__)
            os.chdir(basedir)
            os.chdir('..')

    # apply operation many times as one
    @staticmethod
    def apply(operation, *argslist):
        result = []
        for args in argslist:
            result.append(operation(*args))
        return tuple(result)
