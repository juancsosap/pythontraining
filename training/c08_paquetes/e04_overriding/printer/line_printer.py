#def print(num):            # Override the builtins print() method
#    print('-'*num)         # Recursive call raise RecursionError: maximum recursion depth exceeded

def show(num):
    print('-'*num)

if __name__ == "__main__":
    #print(5)
    show(5)