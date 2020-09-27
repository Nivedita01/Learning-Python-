#function defining an academic_grader system
def  academic_grader(grade):
    if (grade >=  90):
        return "A"
    elif (grade >= 80 and grade <= 89):
        return "B"
    elif(grade >= 70 and grade <= 79):
        return "C"
    elif(grade >=65 and grade <= 69):
        return "D"
    else:
        return"F"
    
    
# This will print a D
print academic_grader(65)
# This will print a A
print academic_grader(95)
# This will print a B
print academic_grader(80)
# This will print a C
print academic_grader(71)
# This will print a F
print academic_grader(50)

