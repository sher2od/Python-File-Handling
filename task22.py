student = 'Input/grades.csv'

count_5 = 0

with open(student, 'r') as f:
    for line in f:
        name, grade = line.strip().split(',')
        if int(grade) == 5:
            count_5 += 1

print("Bahosi 5 bo‘lganlar soni:", count_5)
