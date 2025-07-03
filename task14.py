#TODO 1-usul
'''
file_name = 'Input/students.txt'

with open(file_name, 'r') as f:
    names = [line.strip() for line in f]

sorted_names = sorted(names, reverse=True)

print("Teskari alfavit boyicha tartiblangan ismlar:")
for name in sorted_names:
    print(name)
'''


#TODO 2-usul

with open("Input/students.txt") as f:
    content = f.read()

names = content.split()
reversed_names = list(map(
    lambda name: name[::-1],
    names
))

with open("Output/output14.txt","w") as f:
    f.write(f"\n".join(reversed_names))
