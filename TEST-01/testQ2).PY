#Write a program to calculate simple interest based on Principal, Rate and Time (SI = P*R*T/100)

P = int(input("enter the initial amount borrowed or invested ="))
R = int(input("enter the rate of intereset per annum ="))
T = int(input("enter the time ="))

SI = (P * R * T) / 100

print(f'{SI}Rs')
