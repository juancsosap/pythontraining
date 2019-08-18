def gen_mul(num):
    n = 0
    while(True):
        n += num
        yield n

def main():
    gen1 = gen_mul(3)
    for i in range(10):
        print(next(gen1))
    
    num = 5
    gen2 = ((n+1)*num  for n in range(100))
    for i in range(10):
        print(next(gen2))
    

if __name__ == "__main__":
    main()