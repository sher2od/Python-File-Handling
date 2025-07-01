from collections import Counter

student = 'Input/grades.csv'

grades = []

with open(student, 'r') as f:
    for line in f:
        grades.append(int(line.strip()))

result = Counter(grades)

print(result)
