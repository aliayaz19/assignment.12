# Create a program that asks the user for their scores in different subjects and calculates their 
# overall grade based on a grading scale stored in a dictionary.
# Grading scale dictionary with score ranges
while True:
        
    grading_scale = {
        'A': (90, 100),
        'B': (80, 89),
        'C': (70, 79),
        'D': (60, 69),
        'F': (0, 59)
    }

    programming_Fundamentals = int(input("Enter your total marks in programming_Fundamental: "))
    english = int(input("Enter your total marks in English: "))
    applied_calculus = int(input("Enter your total marks in applied_calculus: "))
    pre_calculus = int(input("Enter your total marks in pre_calculus: "))
    islamic_studies = int(input("Enter your total marks in islamic_studies: "))
    Computer_Fundamentals = int(input("Enter your total marks in Computer_Fundamentals: "))

    total_marks = (programming_Fundamentals + english + pre_calculus + 
                islamic_studies + Computer_Fundamentals + applied_calculus)
    if total_marks >= 90:
        grade = 'A'
    elif total_marks >= 80:
        grade = 'B'
    elif total_marks >= 70:
        grade = 'C'
    elif total_marks >= 60:
        grade = 'D'
    else:
        grade = 'F'
        break
    print(f"Your overall grade is: {grade}")

