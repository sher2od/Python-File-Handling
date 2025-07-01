file_path = 'Input/numbers.txt'

# with open(file_path) as f:
#     nums = [int(line.strip()) for line in f]

# max_num = max(nums)

# print("Eng katta son:", max_num)

file = open(file_path, 'r')

nums = []
for i in file:
    num = int(i.strip())
    nums.append(num)

file.close()

print(max(nums))
