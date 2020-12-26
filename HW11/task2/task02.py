"""
You are given the following code:
class Order:
    morning_discount = 0.25
    def __init__(self, price):
        self.price = price
    def final_price(self):
        return self.price - self.price * self.morning_discount
Make it possible to use different discount programs.
Hint: use strategy behavioural OOP pattern.
https://refactoring.guru/design-patterns/strategy
Example of the result call:
def morning_discount(order):
    ...
def elder_discount(order):
    ...
order_1 = Order(100, morning_discount)
assert order_1.final_price() == 50
order_2 = Order(100, elder_discount)
assert order_1.final_price() == 10
"""
from abc import abstractmethod


class Order:
    def __init__(self, price, discount):
        self.price = price
        self._discount = discount

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, discount):
        self._discount = discount

    def final_price(self):
        return self._discount.get_final_price(self.price)


class Discount:
    @abstractmethod
    def get_final_price(self, price):
        pass


class MorningDiscount(Discount):
    def get_final_price(self, price):
        return price - price * 0.5


class ElderDiscount(Discount):
    def get_final_price(self, price):
        return price - price * 0.9
