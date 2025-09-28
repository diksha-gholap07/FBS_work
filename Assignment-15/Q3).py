#Create a class Shirt with members as sid,sname,type(formal etc), price and size(small,large etc) .Add following methods:
#g. Constructor (Support both parameterized and parameterless)
#h. Destructor
#i. ShowBook
class Shirt:
    def __init__(self, sid, sname, type, price, size):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size
        print("Object is created")
    
    def __del__(self):
        print("destructor is called")

    def showShirt(self):
      
        print("SHIRT ID:", {self.sid})
        print("SHIRT NAME:", {self.sname})
        print("SHIRT TYPE:", {self.type})
        print("SHIRT PRICE:", {self.price})
        print("SHIRT SIZE:", {self.size})

s1 = Shirt(222, "abc", "formal", 700, "M")
s1.showShirt()
print("#######################################")
s2 = Shirt(444, "mno", "casual", 700, "S")
s2.showShirt()
print("#######################################")
