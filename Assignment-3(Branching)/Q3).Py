#a program to input angles of a triangle and check whether triangle is valid or not.
angle_1 = int(input("Enter the first angle "))
angle_2 = int(input("Enter the second angle"))
angle_3 = int(input("Enter th third angle"))
triangle = angle_1 + angle_2 + angle_3
if triangle == 180: 
    print("The TRIANGLE is vaild")
else:
    print("The TRIANGLE is invaild")