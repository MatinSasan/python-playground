import unittest

#  to test manually: python -m unittest testing.py


class Currency:
    def __init__(self, code, exchange_to_usd):
        self.amount = 0.00
        self.code = code
        self.exchange_to_usd = exchange_to_usd

    def set_amount(self, amount):
        self.amount = amount

    def in_currency(self, amount):
        return amount / self.exchange_to_usd

    def to_usd(self, amount=None):
        to_convert = amount or self.amount
        return to_convert * self.exchange_to_usd

    def __gt__(self, other):
        # greater than
        return self.to_usd() > other.to_usd()

    def __eq__(self, other):
        # equal to
        return self.to_usd() == other.to_usd()

    def __lt__(self, other):
        # less than, <
        return self.to_usd() < other.to_usd()

    def __le__(self, other):
        # less than or equal to, <=
        return self.to_usd() <= other.to_usd()

    def __ge__(self, other):
        # greater than or equal to, >=
        return self.to_usd() >= other.to_usd()


class CurrencyTest(unittest.TestCase):
    def test_create_currency(self):
        pounds = Currency('GBP', 1.21)

        self.assertEqual(pounds.code, 'GBP')
        self.assertEqual(pounds.exchange_to_usd, 1.21)

    def test_set_amount(self):
        pounds = Currency('GBP', 1.21)
        euros = Currency('EUR', 1.07)

        pounds.set_amount(5000)
        euros.set_amount(10)

        self.assertEqual(pounds.amount, 5000)
        self.assertEqual(euros.amount, 10)

    def test_compare_currency(self):
        pounds = Currency('GBP', 1.21)
        euros = Currency('EUR', 1.07)

        pounds.set_amount(5000)
        euros.set_amount(10)

        self.assertTrue(pounds > euros)

    def test_comparison_with_exception(self):
        pounds = Currency('GBP', 1.21)
        pounds.set_amount(1000)

        with self.assertRaises(AttributeError):
            pounds == 1000


# to run test directly
if __name__ == '__main__':
    unittest.main()
