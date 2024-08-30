from item import Item 

class InvoiceItem:
    """
        item for register with purchase quantity and discount
    """

    def __init__(self, item:Item, qty:int, discount:float=0):
        self.item=item 
        self.qty = qty 
        self.discount = discount 
        # private member for sub total method 
        self._sub_total = (item.price * qty) - discount

    def __repr__(self) -> str:
        return "<class 'item'>"
    
    def __str__(self) -> str:
        return f"Item: {self.item.name}, Quantity: {self.qty}, Discount: ${self.discount}, Total: ${self.get_sub_total():.2f}"

    
    def get_sub_total(self):
        return self._sub_total 