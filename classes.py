class Product:
  def __init__(self, name, cost, price, stock):
    self.name = name
    self.cost = cost
    self.price = price
    self.stock = stock
  def net(self):
    return self.price - self.cost