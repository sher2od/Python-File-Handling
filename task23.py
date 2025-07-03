with open("Input/grades.csv") as f:
    f.readline()
    lines = f.read().split()

    grades = dict()
    for line in lines:
        name,grade = line.split(',')
        grades.setdefault(grade,[]).append(name)

print(grades)