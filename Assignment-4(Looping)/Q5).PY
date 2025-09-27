#WAP to print Fibonacci series upto n.
num = int(input("enter the number to get fibonacci series"))
a = -1
b = 1 
for i in range (num):
    c = a + b
    print (c, end = '')
    a = b
    b = c