#WAP to print all odd numbers until n.
n = int(input("Enter the number up to which you want odd numbers:"))

print("odd numbers upto", n, "are:")

for i in range(1, n+1, 2):
    print(i, end=" ")