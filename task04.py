file_path = 'Input/numbers.txt'

file = open(file_path, 'r')

nums = []
for i in file:
    number = int(i.strip())
    if number % 2 == 0:
        nums.append(number)

file.close()

print(nums)
