#def print(msg):            # Override the builtins print() method
#    print(msg)             # Recursive call raise RecursionError: maximum recursion depth exceeded

def show(msg):
    print(msg)

if __name__ == "__main__":
    #print('hola')
    show('hola')