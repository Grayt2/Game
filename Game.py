import time
global u1
global cash
u1 = 0
cash = 10
save_data = str(input("Enter save string: "))
def saveString_decompile(save_data):
  global u1, cash
  save_list = save_data.split(".")
  u1 = u1 + int(save_list[0])
  cash = cash + int(save_list[-1])
def Game():
  time_atstart = time.time()
  global cash, u1
  class upgrade_1:
    def __init__(self, number_of_upgrades, cash):
      self.cash = cash
      self.number_of_upgrades = number_of_upgrades
    def formula(self):
      self.cash = self.cash + ((self.number_of_upgrades/10)+0.2)
      return self.cash
    def Buy_u1(self):
      if cash > 20 + (self.number_of_upgrades/0.9):
        self.cash = self.cash - (20 + (self.number_of_upgrades/0.9))
      else:
        print("To little funds.")
  p = upgrade_1(u1, cash)
  cash = p.formula()
  print(f"{round(cash, 3)}$")
saveString_decompile(save_data)
for i in range(20):
  time.sleep(1)
  Game()
  
  
