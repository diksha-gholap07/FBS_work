ticket = float(input("Enter ticket amount per person = "))
total = 0

for i in range(1,6):
    age = int(input("Enter age of perso {i} : ")) 

    if age < 12:
       pay = ticket * 0.7
    elif age > 59:
        pay = ticket * 0.5
    else:
        pay = ticket
    print(f"person {i} will pay: {pay}")
    total += pay

print("Total Amount to be paid =", total)