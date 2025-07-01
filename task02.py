file_path = 'Input/numbers.txt'

# s = 0
# with open(file_path) as f:
#     for line in f:
#         s += int(line.strip())

# print(s)


f = open(file_path,'r')

s = 0
for i in f:
    s += int(i.strip())

print(s)
f.close()


