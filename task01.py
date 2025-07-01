file_path = 'Input/numbers.txt'

with open(file_path) as f:
    nums = list(map(
        lambda number_str: int(number_str.strip()),
        f.read().split()
    ))

print(nums)