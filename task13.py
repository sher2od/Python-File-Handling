file_name = 'Input/students.txt'

with open(file_name, 'r') as f:
    names = [line.strip() for line in f]

sorted_names = sorted(names)

print("Alfavit boyicha tartiblangan ismlar:")
for name in sorted_names:
    print(name)
