

class Money:
    
    amount = 0
    currency_str = ""
    
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency_str = currency

    def __eq__(self, other) -> bool:
        return self.equals(other)
    
    def __str__(self) -> str:
        return str(self.amount) + " " + self.currency_str

    def equals(self, object) -> bool:
        a = self
        b = object
        return self.amount == object.amount and \
            self.currency().__eq__(object.currency())

    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency_str)      

    def currency(self):
        return self.currency_str

    @staticmethod
    def dollar(amount):
        return Money(amount, "USD")

    @staticmethod
    def franc(amount):
        return Money(amount, "CHF")
