#Write a program to check if user has entered correct userid and password.
userid = input("enter your userid:")
password = input("Enter your password:")

if userid == "12345" and password == "6789":
    print("The userid and password is Vaild.")

elif userid == "12345" and password != "6789":
    print("invaild password.")

elif userid != "12345" and password == "6789":    
    print("The userid is invaild.") 
    
else:
    print("invaild userid and password.") 
