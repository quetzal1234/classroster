import csv
import tkinter
print("This program creates a text file that can be copy and pasted to compass.")
print("You will be prompted to open a .csv. Your csv must contain the following columns in the following order:")
print("1. First Name, 2. Last Name, 3. netid, 4. email, 5. linkedin, 6. group")
print("Please use the same column headers (without the numbers).")
from tkinter.filedialog import askopenfilename
filename = askopenfilename()

infile = open(filename, "r", encoding="utf-8")
outfile = open("roster.txt", "w", encoding="utf-8")

csvin = csv.reader(infile)
headers = next(csvin)
groups = dict()
for line in csvin:
    student = line
    group = line[5]
    if group not in groups:
        groups[group]=[student]
    else:
        groups[group].append(student)

def missinglink(linkedin,firstname,lastname):
    if linkedin == "":
        linkedinline = " "
    else:
        linkedinline = '<a href="'+linkedin+'"><img src="http://i.imgur.com/Z9pDAGI.png" alt="Linkedin profile: '+firstname+" "+lastname+'" height="15px" width="15px" margin="1px" /></a> '
    return linkedinline

for key in groups:
    students = groups[key]
    groupline = "</p><h2>Group "+key+"</h2> \n<p>"
    outfile.write(groupline)
    for student in students:
        firstname = student[0]
        lastname = student[1]
        email = student[3]
        linkedin = student[4]
        nameline = firstname+" "+lastname+" "
        emailline = "<a href = "+"'mailto:"+email+"'>"+email+"</a>, \n"
        studenthtml = nameline+missinglink(linkedin,firstname,lastname)+emailline
        outfile.write(studenthtml)
outfile.close()
infile.close()
