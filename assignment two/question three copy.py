#WITI has tasked you to automate a simple grading system 
#As a python student, write a program used to display the
#  grades that the student will be receiving based on the mark 
#scored in a subject.The grades are:
#90% - 100% Grade is A
#80% - 89% Grade is B
#70% - 79% Grade is C
#60% - 69% Grade is D
#50% - 59% Grade is E
# < 50% Fail

#answers
def get_grade(marks):
    if 90 <= marks <= 100:
        return'A'
    elif 80 <= marks < 90:
        return'B'
    elif 70 <= marks <80:
        return'C'
    elif 60 <= marks <70:
        return'D'
    elif 50 <= marks <60:
        return'E'
    elif 0 <= marks <50:
        return 'Fail'
    else:
        return 'Invalid marks'
    #students marks
    marks = float(input("Enter the studen's marks (0-100):"))
    #display of grades
    grade = get_grade(marks)
    print(f"The student's grade is: {grade}")
