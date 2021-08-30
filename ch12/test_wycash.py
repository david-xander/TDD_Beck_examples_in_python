from wycash import Money, Bank
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

if __name__ == '__main__':
    unittest.main()  # pragma: no cover
