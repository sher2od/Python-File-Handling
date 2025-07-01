file_path = 'Input/numbers.txt'


kv_nums = []

with open(file_path,'r') as f:
    num = list(map(lambda n: pow(int(n.strip()),2),f))
    kv_nums.append(num)

print(kv_nums)