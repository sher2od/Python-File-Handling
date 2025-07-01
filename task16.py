file_name = 'Input/students.txt'

with open(file_name, 'r') as f:
    names = [line.strip() for line in f]

print("5 ta harfdan uzun talabalar ")


first = []
for i in names:
    if len(i) > 5:
        first.append(i)

print(first)