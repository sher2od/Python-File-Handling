
student = 'Input/grades.csv'

with open(student, 'r') as f:
    red = list(map(lambda m: str(m.strip()), f))

print(red)
