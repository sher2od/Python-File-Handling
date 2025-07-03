# #TODO 1-usul

# file_path = 'Input/numbers.txt'

# s = []
# with open(file_path, 'r') as f:
#     num = list(map(lambda n: len(str(abs(int(n.strip())))), f))
#     s += num

# print(s)


#TODO 2-usul

with open("Input/numbers.txt") as f:
    content = f.read()

nums = content.split()
result = list(map(
    lambda num: f"{num} : {len(num)} xona",
    nums
))

with open("Output/output09.txt","w") as f:
    f.write("\n".join(result))