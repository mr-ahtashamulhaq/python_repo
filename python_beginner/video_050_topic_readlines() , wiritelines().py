#  Read a file line by line using readline() and print each line with line numbers.

with open("input1.txt", "r") as f:
    i = 1
    while True:
        line = f.readline()
        if not line:
            break
        print(f"Line {i}: {line.strip()}")
        i += 1



#  Read 5 lines from user and write them to a file using writelines().

lines = []
for i in range(5):
    user_input = input(f"Enter line {i+1}: ") + "\n"
    lines.append(user_input)

with open("output2.txt", "w") as f:
    f.writelines(lines)



#  Read all lines from one file using readline() and write only lines containing the word 'Python' to another file using writelines().

with open("input3.txt", "r") as f:
    lines_to_write = []
    while True:
        line = f.readline()
        if not line:
            break
        if "Python" in line:
            lines_to_write.append(line)

with open("output3.txt", "w") as f_out:
    f_out.writelines(lines_to_write)



# Read a CSV file using readline(), split by comma, and write formatted marks statements to another file using writelines().

with open("marks_input4.csv", "r") as f:
    output_lines = []
    student_num = 1
    while True:
        line = f.readline()
        if not line:
            break
        parts = line.strip().split(",")
        m1 = parts[0]
        m2 = parts[1]
        m3 = parts[2]
        output_lines.append(f"Marks of student {student_num} in Maths: {m1}\n")
        output_lines.append(f"Marks of student {student_num} in English: {m2}\n")
        output_lines.append(f"Marks of student {student_num} in SST: {m3}\n")
        output_lines.append("\n")
        student_num += 1

with open("marks_output4.txt", "w") as f_out:
    f_out.writelines(output_lines)



#  Create a file with 10 lines using writelines(), then read it using readline() and print only lines with even line numbers.

lines = [f"This is line {i+1}\n" for i in range(10)]
with open("input5.txt", "w") as f:
    f.writelines(lines)

with open("input5.txt", "r") as f:
    line_num = 1
    while True:
        line = f.readline()
        if not line:
            break
        if line_num % 2 == 0:
            print(f"Even Line {line_num}: {line.strip()}")
        line_num += 1