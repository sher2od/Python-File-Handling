
#TODO 1-usul 

'''
# file_path = 'Input/numbers.txt'

# # with open(file_path) as f:
# #     nums = [int(line.strip()) for line in f]

# # max_num = max(nums)

# # print("Eng katta son:", max_num)

# file = open(file_path, 'r')

# nums = []
# for i in file:
#     num = int(i.strip())
#     nums.append(num)

# file.close()

# print(max(nums))'''


#TODO 2-usul

with open("Input/numbers.txt") as f:
    content = f.read()

nums = content.split()
max_number = max(nums,key=int)

with open("Output/output03.txt","w") as f:
    f.write(f"Max: {max_number}")
