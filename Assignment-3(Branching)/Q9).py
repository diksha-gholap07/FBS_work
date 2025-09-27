#Input 5 subject marks from user and display grade(eg.First class,Second class ..)
English = float(input("Enter the marks obtained in English : ")) #enter the marks 50 out of 
Maths = float(input("Enter the marks obtained in Maths: "))
Science = float(input("Enter the marks obtained in Science : "))
History = float(input("Enter the marks obtained in History: "))
Geography = float(input("Enter the marks obtained in Geography : "))

Total_marks_obtained = English + Maths + Science + History + Geography

if Total_marks_obtained >= 220:
    print("Grade = Distinction.")
elif Total_marks_obtained >= 200:
    print("Grade = First class.")
elif Total_marks_obtained >= 180:
    print("Grade = Second class.")
elif Total_marks_obtained >= 120:
     print("Grade = need to study hard.")

else:
     print("Grade = fail.")