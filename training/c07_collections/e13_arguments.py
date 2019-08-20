import sys

result = 0
for num in sys.argv[1:]:
    num = int(num)
    print(num)
    result += num

print('-'*10)
print(result)
     