#WAP to print all numbers in a range divisible by a given number.
start = int(input("enter the start of the range:"))
end = int(input("enter the end of the range:"))

divisor = int(input("enter the number to check divisibility:"))

print(f"numbers divisible by {divisor} in the range {start} to {end} are:")


for i in range(start, end + 1):
    if i % divisor == 0:
        print(i, end=" ")