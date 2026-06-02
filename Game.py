import time
global time
time = time.time()
class save_game:
    global time
    try:
        f = open("/home/lumi/Documents/Python_Game/Cash", "x")
    except:
        f = open("/home/lumi/Documents/Python_Game/Cash", "a")
        f.write(f"")

def Game():
    class upgrade_1:
        def __init__(self, number_of_upgrades):
            self.number_of_upgrades = number_of_upgrades
        