from abc import ABC, abstractmethod


class Expression(ABC):
    def reduce(to):
        pass

class Bank:
    def reduce(self, source, to):
        return source.reduce(to)

class Sum(Expression):
    augend=None
    addend=None

    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend
    
    def reduce(self, to):
        amount = self.augend.amount + self.addend.amount
        return Money(amount, to)


class Money(Expression):
    amount = 0
    currency_str = ""
    
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency_str = currency

    def __eq__(self, other) -> bool:
        # better keeping python way
        return self.amount == other.amount and \
            self.currency()== other.currency()        

    def __add__(self, addend):
        return Sum(self, addend)

    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency_str)      

    def currency(self):
        return self.currency_str

    def reduce(self, to):
        return self

    @staticmethod
    def dollar(amount):
        return Money(amount, "USD")

    @staticmethod
    def franc(amount):
        return Money(amount, "CHF")


if __name__ == '__main__':
    print(Money.dollar(10) == (Money.dollar(5) + Money.dollar(5)))
