numbers = tuple([float(num) for num in input().split()])
occ = {}

for num in numbers:
    occ[num] = numbers.count(num)

for num, count in occ.items():
    print(f"{num} - {count} times")