file_path = 'Input/numbers.txt'

with open(file_path, 'r') as f:
    k5_num = list(map(lambda n: int(n.strip()), filter(lambda n: int(n.strip()) % 5 == 0, f)))

print(k5_num)
