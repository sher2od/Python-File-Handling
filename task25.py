input_file = 'Input/grades.csv'
output_file = 'Input/high_scores.csv'

with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
    for line in f_in:
        name, grade = line.strip().split(',')
        if int(grade) == 5:
            f_out.write(line)
