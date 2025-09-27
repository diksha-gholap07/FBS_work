#WAP to print all integers upto n that aren’t divisible by 2 and 3.
n = int(input("enter the upper limit:"))
print("numbers divisible by 2 and 3 upto", n, "are:")

for i in range(6, n+1, 6):
    print(i, end=" ")
    