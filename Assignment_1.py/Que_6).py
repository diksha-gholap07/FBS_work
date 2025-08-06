#third angle of triangle
angle_one = int(input("enter one angle of the triangle in degrees: ")) 
angle_two = int(input("enter second angle of the triangle in degrees :"))
angle_third = 180 - (angle_one + angle_two)
print(f'third angle of triangle is : {angle_third} degrees')