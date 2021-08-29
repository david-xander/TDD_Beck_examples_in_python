from wycash import Dollar
import unittest 

class TestWyCash(unittest.TestCase):
    

    def test_multiplication(self):
        five = Dollar(5)
        five.times(2)
        self.assertEqual(10, five.ammount)

if __name__ == '__main__':
    unittest.main()  # pragma: no cover
