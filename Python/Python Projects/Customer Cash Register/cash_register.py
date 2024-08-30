import json
from datetime import datetime

from customer import Customer
from invoice_items import InvoiceItem
from item import Item

class CashRegister:

    """ Cash register for customers"""

    def __init__(self, customer:Customer) -> None:
        self.customer=customer
        self.items: dict[str, InvoiceItem] = {}
        self.purchase_date = datetime.now()
        # private member 
        self._invoice_total: float = 0

    def __repr__(self)->str:
        return "<class 'CashRegister'>"

    def __str__(self) -> str:
        return f"Customer: {self.customer}, total items: {len(self.items)}"

    #private method
    def _inc_invoice_total(self, item: InvoiceItem) -> None:
        """Increase the total invoice amount """
        self._invoice_total += item.get_sub_total()

    def _dec_invoice_total(self, item: InvoiceItem) -> None:
        """Decrease the total invoice amount """
        self._invoice_total -= item.get_sub_total()

    def add_item(self, item: Item, qty: int, discount: float = 0) ->None:
        """ Add an item to cash register"""
        if item.name not in self.items: 
            new_item = InvoiceItem(item, qty, discount)
            self.items[item.name] = new_item
            self._inc_invoice_total(new_item)
        else: 
            print(f"{item.name} already in cart!")


    def update_item(self, item: Item, qty: int, discount: float = 0) ->None:
        """ Update an item to cash register"""
        if item.name in self.items: 
            old_item = self.items[item.name]
            self._dec_invoice_total(old_item)

            new_item = InvoiceItem(item, qty, discount)
            self.items[item.name] = new_item
            self._inc_invoice_total(new_item)
        else: 
            print(f"{item.name} not in cart!")

    
    def delete_item(self, item:Item):
        """ Delete an item from the register"""
        if item.name in self.items:
            old_item = self.items[item.name]
            self._dec_invoice_total(old_item)

            del self.items[item.name]

    def get_invoice_total(self)-> float:
        return self._invoice_total 

    def display_invoice(self)-> None:
        print('='*50)
        print(self)
        print(f"Date: {self.purchase_date.strftime('%B %d, %Y')}")
        print('-'*50)
        for item in self.items.values():
            print(item)
        print("-"*50)
        print(f"Total Price: ${self.get_invoice_total():.2f}")
        print('='*50)
