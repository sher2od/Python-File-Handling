file_path = 'Input/numbers.txt'

# Fayldan sonlarni o‘qib olish
with open(file_path, 'r') as f:
    nums = list(map(lambda line: int(line.strip()), f))


sort_num = sorted(nums)

# Yangi faylga yozish
with open('sorted_numbers.txt', 'w') as f_open:
    for num in sort_num:
        f_open.write(str(num) + '\n')

