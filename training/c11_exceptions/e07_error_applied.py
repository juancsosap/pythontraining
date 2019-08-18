def is_int(text):
    try:
        int(text)
        return True
    except:
        return False

if __name__ == "__main__":
    num = input('Number: ')
    if(is_int(num)):
        print('Result:', int(num)**2)
    else:
        print('Invalid Input')