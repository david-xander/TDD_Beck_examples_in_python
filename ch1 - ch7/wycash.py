

class Money:
    
    amount = 0

    # needed for assertEquals()
    def __eq__(self, other) -> bool:
        return self.equals(other)

    def equals(self, object) -> bool:
        a = self
        b = object
        return self.amount == object.amount and \
            type(a) == type(b)


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
    