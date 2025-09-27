#Write a program to prompt user to enter userid and password. 
# After verifying userid and password display a 4 digit random number and ask user to enter thesame. 
# If user enters the same number then show him success message otherwise
#failed.
userid = input("enter your userid:")
password = input("Enter your password:")

if userid == "12345" and password == "6789":
    print("The userid and password is Vaild.")
    print("now please enter this number : 99 ")
    enter_the_number = int(input("Enter the number provided : "))
    if enter_the_number == 99:
        print("Successs")
    else:
        print("Failed")


elif userid == "12345" and password != "6789":
    print("invaild password.")

elif userid != "12345" and password == "6789":    
    print("The userid is invaild.") 
    
else:
    print("invaild userid and password.") 

