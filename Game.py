import time
cash = 10
save_data = str(input("Enter save string: "))
def Game():
  time_atstart = time.time()
  global cash
  class upgrade_1:
    def __init__(self, number_of_upgrades, cash):
      self.cash = cash
      self.number_of_upgrades = number_of_upgrades
    def formula(self):
      self.cash = self.cash * ((self.number_of_upgrades/6)+1)
      return self.cash
  p = upgrade_1(1, cash)
  cash = p.formula()
  return cash
print(Game())
  
  
