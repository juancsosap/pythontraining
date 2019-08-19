def get_calc(num1, num2, oper):
    def add(): return num1 + num2
    def sub(): return num1 - num2
    def mul(): return num1 * num2
    def div(): return num1 // num2
    
    if(oper == 'A'): return add
    if(oper == 'S'): return sub
    if(oper == 'M'): return mul
    if(oper == 'D'): return div

def get_rel(num1, num2, rel):
    gt = lambda : num1 > num2
    lt = lambda : num1 < num2
    ge = lambda : num1 >= num2
    le = lambda : num1 <= num2
    eq = lambda : num1 == num2
    ne = lambda : num1 != num2
    
    if(rel == 'gt'): return gt
    if(rel == 'lt'): return lt
    if(rel == 'ge'): return ge
    if(rel == 'le'): return le
    if(rel == 'eq'): return eq
    if(rel == 'ne'): return ne

if __name__ == "__main__":
    oper = get_calc(5, 5, 'A')
    print('ADD:', oper())

    oper = get_calc(5, 5, 'S')
    print('SUB:', oper())

    oper = get_calc(5, 5, 'M')
    print('MUL:', oper())

    oper = get_calc(5, 5, 'D')
    print('DIV:', oper())

    print()

    rel = get_rel(5, 7, 'gt')
    print('GT:', rel())

    rel = get_rel(5, 7, 'lt')
    print('LT:', rel())

    rel = get_rel(5, 7, 'ge')
    print('GE:', rel())

    rel = get_rel(5, 7, 'le')
    print('LE:', rel())

    rel = get_rel(5, 7, 'eq')
    print('EQ:', rel())

    rel = get_rel(5, 7, 'ne')
    print('NE:', rel())
