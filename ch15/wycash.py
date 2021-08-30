from abc import ABC, abstractmethod


class Bank:
    rates = {}

    def reduce(self, source, to):
        return source.reduce(self, to)
    
    def addRate(self, currency_from, currency_to, rate):
        # we don't use Pair and the HashMap and HashTable
        # instead, let's use the hash table dict() builtin in py
        # (all the HashMap/HashTable DS I have to build it my own)
        # I think it's out of scope in python
        self.rates[currency_from + " > " + currency_to]=rate
        return rate
    
    def rate(self, currency_from, currency_to):
        if currency_from == currency_to: return 1
        rate = self.rates.get(currency_from + " > " + currency_to)
        return rate


class Expression(ABC):
    def reduce(bank, to):
        pass
    
    def __add__(self, addend):
        pass

class Sum(Expression):
    augend=None
    addend=None

    def __init__(self, augend: Expression, addend: Expression):
        self.augend = augend
        self.addend = addend
    
    def __add__(self, addend):
        return None

    def reduce(self, bank, to):
        amount = self.augend.reduce(bank, to).amount \
            + self.addend.reduce(bank, to).amount
        return Money(amount, to)

    def rate(self, currency_from, currency_to):
        rate = 1
        if currency_from == "CHF" and currency_to == "USD":
            rate = 2
        return rate

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

    def __add__(self, addend: Expression):
        return Sum(self, addend)

    def times(self, multiplier: int) -> Expression:
        return Money(self.amount * multiplier, self.currency_str)      

    def currency(self):
        return self.currency_str

    def reduce(self, bank, to):
        rate = bank.rate(self.currency(), to)
        return Money(self.amount / rate, to)

    @staticmethod
    def dollar(amount):
        return Money(amount, "USD")

    @staticmethod
    def franc(amount):
        return Money(amount, "CHF")


if __name__ == '__main__':
    print(Bank().rate("USD", "USD"))
