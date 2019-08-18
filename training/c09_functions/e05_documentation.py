def factorial(num):
    '''    Return the number factorial
    If the number is 1 or less, return 1'''
    if num > 1:
        return num * factorial(num -1)
    else:
        return 1 

def main():
    print(factorial.__doc__)
    help(factorial)

if __name__ == "__main__":
    main()