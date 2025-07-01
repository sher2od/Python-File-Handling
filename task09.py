file_path = 'Input/numbers.txt'

s = []
with open(file_path, 'r') as f:
    num = list(map(lambda n: len(str(abs(int(n.strip())))), f))
    s += num

print(s)
