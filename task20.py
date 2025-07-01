student = 'Input/grades.csv'

with open(student, 'r') as f:
    grades = list(map(lambda x: int(x.strip()), f))

average = sum(grades) / len(grades)

print("O'rtacha baho:", average)
