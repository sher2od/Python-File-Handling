file_path = 'Input/numbers.txt'

with open(file_path, 'r') as f:
    nums = list(map(lambda line: int(line.strip()), f))

with open('odd_numbers.txt', 'w') as f_open:
    for num in nums:
        if num % 2 != 0:
            f_open.write(str(num) + '\n')
