from wycash import Money, Bank, Sum
import unittest 

class TestWyCash(unittest.TestCase):

    def test_multiplication(self):
        five = Money.dollar(5)
        self.assertEqual(Money.dollar(10), five.times(2))
        self.assertEqual(Money.dollar(15), five.times(3))

    def test_equality(self):
        # refactoring to keep it pythonic
        self.assertEqual( Money.dollar(5), Money.dollar(5) )
        self.assertNotEqual( Money.dollar(5), Money.dollar(6) )
        self.assertNotEqual( Money.franc(5), Money.dollar(5) )

    def test_currency(self):
        self.assertEqual("USD", Money.dollar(1).currency())
        self.assertEqual("CHF", Money.franc(1).currency())

    def test_simple_addition(self):
        five = Money.dollar(5)
        sum = five + five
        bank = Bank()
        reduced = bank.reduce(sum, "USD")
        self.assertEqual(Money.dollar(10), reduced)

    def test_plus_returns_sum(self):
        five = Money.dollar(5)
        sum = five + five
        self.assertEqual(five, sum.augend)
        self.assertEqual(five, sum.addend)
    
    def test_reduce_sum(self):
        sum = Money.dollar(3) + Money.dollar(4)
        bank = Bank()
        result = bank.reduce(sum, "USD")
        self.assertEqual(Money.dollar(7), result)

    def test_reduce_money(self):
        bank = Bank()
        result = bank.reduce(Money.dollar(1), "USD")
        self.assertEqual(Money.dollar(1), result)        

    def test_reduce_money_different(self):
        bank = Bank()
        bank.addRate("CHF", "USD", 2)
        result = bank.reduce(Money.franc(2), "USD")
        self.assertEqual(Money.dollar(1), result)   

    def test_identity_rate(self):
        self.assertEqual(1, Bank().rate("USD", "USD"))  
    
    def test_mixed_addition(self):
        fiveBucks = Money.dollar(5)
        tenFrancs = Money.franc(10)
        bank = Bank()
        bank.addRate("CHF", "USD", 2)
        result = bank.reduce(fiveBucks + tenFrancs, "USD")
        self.assertEqual(Money.dollar(10), result)


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
