

class Money:
    
    amount = 0
    currency_str = ""
    
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency_str = currency

    def __eq__(self, other) -> bool:
        return self.equals(other)

    def equals(self, object) -> bool:
        a = self
        b = object
        return self.amount == object.amount and \
            type(a) == type(b)

    def currency(self):
        return self.currency_str

    @staticmethod
    def dollar(amount):
        return Dollar(amount, "USD")

    @staticmethod
    def franc(amount):
        return Franc(amount, "CHF")

class Dollar(Money):
    
    def times(self, multiplier):
        return Money.dollar(self.amount * multiplier) 

class Franc(Money): 

    def times(self, multiplier):
        return Money.franc(self.amount * multiplier)      
