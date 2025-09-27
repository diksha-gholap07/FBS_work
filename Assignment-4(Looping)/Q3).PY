#WAP to print sum of series upto n.
n = int(input("enter the value of n:"))
sum_series = 0

for i in range(1, n+1):
    sum_series += i

print("sum of the series", n, "is", sum_series)