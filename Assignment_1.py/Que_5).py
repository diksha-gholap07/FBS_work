#compound interest
P = float(input("enter the initial amount borrowed or invested ="))
r = float(input("enter the rate of intereset per annum ="))
N = float(input("enter the number of times interest is compounded per year"))
T = float(input("enter the time ="))
R = r / 100
A = P * (1 + R / N) ** (N * T)
CI = A - P
print(f'total amount after {T} years = {A}')
print(f'compound interest is = {CI}Rs')
