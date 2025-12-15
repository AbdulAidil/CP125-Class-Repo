#ABDUL AIDIL SHAH BIN AJIBIR
#This program checks the grade for one student

def determine_grade (mark):
    if mark >= 80:
        return "A"
    elif mark >= 60:
        return "B"
    elif mark >= 50:
        return "C"
    elif mark >= 40:
        return "D"
    else:
        return "F"

#Get the input from the user
mark = float(input("Enter the student's mark: "))

#Display the student’s mark and grade
#Call determine_grade function to get the grade based on the input
print(f"Mark: {mark}, Grade: {determine_grade(mark)}")
