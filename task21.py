student = 'Input/grades.csv'

top_student = ""
top_grade = -1

with open(student, 'r') as f:
    for line in f:
        name, grade = line.strip().split(',')
        grade = int(grade)
        if grade > top_grade:
            top_grade = grade
            top_student = name

print("Eng yuqori baho olgan oquvchi:", top_student, "-", top_grade)
