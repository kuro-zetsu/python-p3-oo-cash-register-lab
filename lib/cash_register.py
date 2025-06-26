#!/usr/bin/env python3

class CashRegister:

  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0.0
    self.items = []
    self.last_item = []
    self.last_price = 0.0
    self.prices = []
    self.items_tracker = []

  @property
  def discount(self):
    return self._discount
  
  @discount.setter
  def discount(self, new_discount):
    if isinstance(new_discount, (int, float)) and new_discount >= 0:
      self._discount = new_discount
    else:
      raise ValueError("Discount must be a positive number.")


  def add_item(self, title, price, quantity = 1):
    if not all(isinstance(x, (int, float)) for x in (price, quantity)):
      raise ValueError("Price and quantity must be numbers.")
    
    if not all((y > 0) for y in (price, quantity)):
      raise ValueError("Price and quantity must be positive.")
    
    self.last_price = round(float(price), 2) * quantity
    self.total += self.last_price
    self.prices.append(self.last_price)
  
    if not isinstance(title, str) or len(title) == 0:
      raise ValueError("Title must be a non-empty string.")
    
    self.last_item = [title for _ in range(quantity)]
    self.items.extend(self.last_item)
    self.items_tracker.append(self.last_item)
    
  def apply_discount(self):
    if self._discount != 0:
      self.total *= (100 - self._discount) / 100
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    if not self.items_tracker:
      print("No transaction to void.")
      return
    
    last_item = self.items_tracker.pop()
    last_amount = self.prices.pop()
    del self.items[-len(last_item):]
    self.total = round(self.total - last_amount, 2)


