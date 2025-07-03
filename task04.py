# #TODO 1 - usul

# file_path = 'Input/numbers.txt'

# file = open(file_path, 'r')

# nums = []
# for i in file:
#     number = int(i.strip())
#     if number % 2 == 0:
#         nums.append(number)

# file.close()

# print(nums)


#TODO 2-usul 


with open("Input/numbers.txt") as f:
    content = f.read()

nums = content.split()
evens = list(filter(
    lambda num: int(num) % 2 == 0,
    nums
))


text = ", ".join(evens)

with open("Output/output04.txt","w") as f:
    f.write(f"Evens:{text}")

