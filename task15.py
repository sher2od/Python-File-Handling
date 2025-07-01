file_name = 'Input/students.txt'

with open(file_name, 'r') as f:
    names = [line.strip() for line in f]

print("Ismlar va ularning harflar soni:")
for name in names:
    print(f"{name} - {len(name)} ta harf")
