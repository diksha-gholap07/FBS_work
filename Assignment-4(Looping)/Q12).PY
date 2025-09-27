#WAP to print Armstrong number within a given range
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

print(f"Armstrong numbers between {start} and {end} are:")

for num in range(start, end + 1):
    sum_of_cubes = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum_of_cubes += digit ** 3
        temp //= 10
    if sum_of_cubes == num:
        print(num, end=" ")