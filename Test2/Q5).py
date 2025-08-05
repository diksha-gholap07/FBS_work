product_1 = int(input("enter price of product 1="))
product_2 = int(input("enter price of product 2="))
product_3 = int(input("enter price of product 3="))
product_4 = int(input("enter price of product 4="))
product_5 = int(input("enter price of product 5="))

#total_bill = sum of all product + 18% GST 
sum_of_product = (product_1 + product_2 + product_3 + product_4 + product_5) 
total_bill =  sum_of_product + (sum_of_product * 18 / 100)
print(f'{total_bill} is the total bill with 18% GST')