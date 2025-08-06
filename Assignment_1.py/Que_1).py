#program to calculate percentage of students
english = int(input("Enter the marks obtained in english="))
maths = int(input("Enter the marks obtained in maths="))
science = int(input("Enter the marks obtained in science="))
history = int(input("Enter the marks obtained in history="))
geography = int(input("Enter the marks obtained in geography="))

total_marks_obtained = english + maths + science + history + geography

percentage_obtained = (total_marks_obtained / 500) * 100

print(f'{percentage_obtained}%.')
