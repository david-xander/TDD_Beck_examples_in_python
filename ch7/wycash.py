

class Money:
    
    amount = 0
    
    def __eq__(self, other) -> bool:
        return self.equals(other)

    def equals(self, object) -> bool:
        a = self
        b = object
        return self.amount == object.amount and \
            type(a) == type(b)

    @staticmethod
    def dollar(amount):
        return Dollar(amount)

    @staticmethod
    def franc(amount):
        return Franc(amount)

class Dollar(Money):
    def __init__(self, amount):
        self.amount = amount
        
    def times(self, multiplier):
        return Dollar(self.amount * multiplier) 

class Franc(Money):
    def __init__(self, amount):
        self.amount = amount
             
    def times(self, multiplier):
        return Franc(self.amount * multiplier)    
