#Write a program to find the area and perimeter of following figure 
length = int(input("enter the length of the rectangle"))
width = int(input("enter the width of the rectangle"))
radius = int(input("enter the radius "))

Areaofrectangle = length * width
perimeterofrectangle = 2 * (length + width)
Areaofsemicircle = (3.14 * radius * radius) / 2
perimeterofsemicircle = (3.14 * radius) + (2 * radius)

print(f'{Areaofrectangle} is the area of rectangle')
print(f'{perimeterofrectangle} is the perimeter of rectangle')
print(f'{Areaofsemicircle} is the area of semicircle')
print(f'{perimeterofsemicircle} is the perimeter of semicircle')