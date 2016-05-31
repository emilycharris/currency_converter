class Money:

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency


    def usd(self):
        if self.currency.upper() == 'USD':
            return self.amount * 1
        if self.currency.upper() == 'EUR':
            return self.amount * 1.11
        if self.currency.upper() == 'JPY':
            return self.amount * .01
        if self.currency.upper() == 'BTC':
            return self.amount * 521.44
        else:
            raise Exception("Please enter USD, EUR, JPY, or BTC")

    def __gt__(self, other):
        return self.usd() > other.usd()

    def __lt__(self, other):
        return self.usd() < other.usd()

    def __eq__(self, other):
        return self.usd() == other.usd()

    def __ge__(self, other):
        return self.usd() >= other.usd()

    def __ne__(self, other):
        return self.usd() != other.usd()

    def __add__(self, other):
        return self.usd() + other.usd()

    def __sub__(self, other):
        return self.usd() - other.usd()

    def __mul__(self, other):
        return self.usd() * other.usd()


value_one = Money(100, 'jpy')
value_two = Money(500, 'eur')
value_three = Money(30, 'btc')
value_four = Money(200, 'usd')

print('Value One USD: ', Money.usd(value_one))
print('Value Two USD:', Money.usd(value_two))
print('Value Three USD:', Money.usd(value_three))
print('Value Four USD:', Money.usd(value_four))
print('\n')
print('Value Four >= Value Two: ', value_four >= value_two)
print('Value One > Value Two: ', value_one > value_two)
print('Value Three <= Value Two: ', value_three <= value_two)
print('Value One < Value Four: ', value_one < value_four)
print('Value Four + Value Two: ', value_four + value_two)
print('Value Four - Value Three: ', value_four - value_three)
print('Value One = Value Three: ', value_one == value_three)
print('Value Three not equal to Value Four: ', value_three != value_four)
print('Value Four * Value Two: ', value_four * value_two)
print('\n')

#### Hard Mode ####
print((Money.usd(Money(100.00, "USD")) + Money.usd(Money(56.32, "EUR"))) + (Money.usd(Money(1.2, "BTC")) + Money.usd(Money(8, "USD"))))

