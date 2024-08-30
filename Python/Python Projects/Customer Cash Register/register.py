from cash_register import CashRegister
from customer import Customer 
from item import Item 

milk = Item(100, "Milk", 4.5, "Litere")
apple = Item(101, "Apple", 20, 'KG')
veg = Item(102,"Vegtables",50, 'KG')
almond = Item(103,'Almond',100,"Grams")


customerOne = Customer("Steve","Smith")

cs = CashRegister(customerOne)
cs.add_item(milk, 1,1)
cs.add_item(almond, 10, 10)
cs.add_item(veg, 10, 2)

# cs.display_invoice()
cs.update_item(milk, 2, 2)
# cs.display_invoice()
cs.add_item(apple, 10, 0)
cs.display_invoice()
cs.delete_item(apple)
cs.display_invoice()

