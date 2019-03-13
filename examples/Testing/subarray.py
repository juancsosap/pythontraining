size = int(input())

numbers = [int(y) for y in input().split(' ')]

count = 0
for i in range(size):
    for j in range(i, size):
        if sum(numbers[i:j + 1]) < 0:
            count += 1

print(count)
