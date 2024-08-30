class Item:
    def __init__(self, id:int, name:str, price:float, unit:str) -> None:
        self.id = id
        self.name= name 
        self.price = price 
        self.unit = unit 

    def __repr__(self)-> str:
        return "<class 'item'>"
        

    def __str__(self) -> str:
        return f"{self.name}: ${self.price}/{self.unit}"