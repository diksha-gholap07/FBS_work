year = int(input("enter any year"))

if (year % 4 == 0):
     print(f'{"leap year"}')
else:
    print(f'{"not a leap year"}')
 
 
if (year % 100 == 0):
    print(f'{"not a leap year"}')
else:
     print(f'{"leap year"}')

if (year % 400 == 0):
      print(f'{"leap year"}')
else:
      print(f'{"not a leap year"}')      
     
    