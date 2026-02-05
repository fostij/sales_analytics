class Entity:
    def __init__(self, id):
        if not id:
            raise ValueError("ID cannot be empty")
        self.id = id
    
    def __repr__(self):
        return f"{self.__class__.__name__} (id={self.id})"
    

class Product(Entity):
    def __init__(self, name, category, base_price):
        super().__init__(id)
        if base_price < 0:
            raise ValueError("Price must be positive")
        self.name = name
        self.category = category
        self.base_price = base_price


class Customer(Entity):
    def __init__(self, name, email, lifetime_value=0.0):
        super().__init__(id)
        if "@" not in email:
            raise ValueError("Invalid email")
        self.name = name
        self.email = email
        self.lifetime_value = lifetime_value


class Order:
    def __init__(self, date, items, customer, amount, status):
        if amount < 0:
            raise ValueError("Emount must be >= 0")
        self.date = date
        self.items = items
        self.customer = customer
        self.amount = amount
        self.status = status