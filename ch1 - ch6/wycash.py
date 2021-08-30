

class Money:
    
    amount = 0
    
    def __init__(self, input, *args, **kwargs):
        super(Money, self).__init__(*args, **kwargs)
        self.amount = input
    
    # needed for assertEquals()
    def __eq__(self, other) -> bool:
        return self.equals(other)

    def equals(self, object) -> bool:
        a = self
        b = object
        return self.amount == object.amount and \
            type(a) == type(b)


class Dollar(Money):
    def times(self, multiplier):
        return Dollar(self.amount * multiplier)    
    

class Franc(Money):
    def times(self, multiplier):
        return Franc(self.amount * multiplier)    
    