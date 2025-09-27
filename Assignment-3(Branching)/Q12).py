#Write a program to check if given 3 digit number is a palindrome or not.
num = int(input("enter a number:"))
temp = num
rev = 0

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10

if num == rev:
    print("The number is a palindrome")

else:
    print("The number is not a palindrome")