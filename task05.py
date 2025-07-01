file_path = 'Input/numbers.txt'

with open(file_path, 'r') as file:
    nums = [int(line.strip()) for line in file]

if nums:  
    average = sum(nums) / len(nums)
    print("O'rtacha qiymat:", average)
else:
    print("Faylda son yo'q!")

