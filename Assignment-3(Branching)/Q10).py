#Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)
Gender = input("Enter the Gender : " )
Age = int(input("Enter the Age : "))

if Gender == "male":
    if Age >= 21:
        print("Eligible for marriage.")
    else:
        print("Not Eligible for marriage.")
elif Gender == "female":
    if Age >= 18:
        print("Eligible for marriage.")
    else:
        print("Not Eligible for marriage.")
else:
    print("envalid gender")