#program to calculate profit or loss.
Cost_price = float(input("Enter the cost price of the product"))
selling_price = float(input("Enter the selling price of product"))


if selling_price > Cost_price:
    profit = selling_price - Cost_price
    print("profit=", profit)
    
else:
     Cost_price > selling_price
     loss = Cost_price - selling_price
     print("loss=", loss)