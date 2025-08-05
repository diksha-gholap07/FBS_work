#Write a program to accept distance in km and convert it into meters and centimeters both.
distance = int(input("enter distance in Km:"))

meters = distance * 1000
centimeter = distance * 100000


print(f'{meters}m {centimeter}cm')

