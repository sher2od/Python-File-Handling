file_name = 'Input/students.txt'

with open(file_name,'r') as f:
    str_file = list(map(lambda m: str(m.strip()),f))

print(str_file)