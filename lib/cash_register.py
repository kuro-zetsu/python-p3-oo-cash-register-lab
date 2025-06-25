#!/usr/bin/env python3

class CashRegister:

  def __init__(self, discount = 0, title = None, price = 0, quantity = 0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.title = title
    self.price = price
    self.quantity = quantity
    self.last_item = []
    self.last_price = 0
    self.prices = []
    self.last_no_of_items = 0
    self.items_tracker = []

  @property
  def price(self):
    return self._price
  
  @price.setter
  def price(self, price):
    if isinstance(price, (int, float)):
      self._price = f"{price:.2f}"
    else:
      print("The price needs to be a number.")


  def add_item(self, title, price, quantity = 1):
    self.last_item = [title for _ in range(quantity)]
    self.items.extend(self.last_item)
    self.items_tracker.append(self.last_item)
    self.last_price = round(float(price), 2) * quantity
    self.total += self.last_price
    self.prices.append(self.last_price)
  
  def apply_discount(self):
    if self.discount != 0:
      self.total *= (100 - self.discount) / 100
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    if self.items != []:
      last_item = self.items_tracker.pop()
      last_amount = self.prices.pop()
      del self.items[-len(last_item):]
      self.total -= last_amount
