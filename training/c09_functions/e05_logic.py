def BOOL(bit):
    return bit != 0

def BIT(line):
    return 1 if line else 0

def NOT(input):
    output = not BOOL(input)
    return BIT(output)

def OR(inputA, inputB):
    output = BOOL(inputA) or BOOL(inputB)
    return BIT(output)

def AND(inputA, inputB):
    output = BOOL(inputA) and BOOL(inputB)
    return BIT(output)

def XOR(inputA, inputB):
    output = OR(AND(NOT(inputA), inputB), AND(inputA, NOT(inputB)))
    return BIT(output)

def ADD(inputA, inputB):
    size = len(inputA)
    output, rest = [], 0
    for i in range(size):
        add = XOR(inputA[-1-i], inputB[-1-i])
        temp = XOR(add, rest)
        rest = OR(AND(add, rest), AND(inputA[-1-i], inputB[-1-i]))
        output.insert(0, BIT(temp))
    output.insert(0, BIT(rest))
    return output

def main():
    print('\n-- NOT')
    print(0, ':', NOT(0))
    print(1, ':', NOT(1))

    print('\n-- OR')
    print(0, 0, ':', OR(0, 0))
    print(0, 1, ':', OR(0, 1))
    print(1, 0, ':', OR(1, 0))
    print(1, 1, ':', OR(1, 1))

    print('\n-- AND')
    print(0, 0, ':', AND(0, 0))
    print(0, 1, ':', AND(0, 1))
    print(1, 0, ':', AND(1, 0))
    print(1, 1, ':', AND(1, 1))

    print('\n-- XOR')
    print(0, 0, ':', XOR(0, 0))
    print(0, 1, ':', XOR(0, 1))
    print(1, 0, ':', XOR(1, 0))
    print(1, 1, ':', XOR(1, 1))

    print('\n-- ADD')
    num1 = [1,0,1,1,0,1]
    num2 = [1,1,1,0,1,1]
    num3 = ADD(num1, num2)
    print(num1, num2, num3, sep='\n')

if __name__ == '__main__':
    main()
