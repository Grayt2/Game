import time
global upgrades, cash

save_data = str(input("Enter save string: "))
if save_data == "":
    upgrades = {1: 1}
    cash = 10

def saveString_decompile(save_data):
    global upgrades, cash
    Save_upgrades = save_data[1:save_data.index("}")+1]
    save_data = save_data[save_data.index("}")+3:]
    save_data = save_data.replace(save_data[-1], "")
    random_variable_name = save_data.split(", ")
    cash = float(random_variable_name[0])
    cash_gain = time.time() - float(random_variable_name[-1]) 
    print(cash)
    return [Save_upgrades, cash, round(cash_gain)]

def upgrades_decompile(upgrades):
    times_ran = 0
    list_keys = []
    list_values = []
    dict_fixed = {}
    list_upgrades = upgrades.split(": ")
    list_upgrades[0] = list_upgrades[0].replace("{", "")
    list_upgrades[-1] = list_upgrades[-1].replace("}", "")
    for i in list_upgrades:
        try:
            if times_ran % 2 == 0:
                list_keys.append(i)
            else:
                list_values.append(i)
                dict_fixed[int(list_keys[-1])] = int(i)
        except ValueError:
            print("error", i)
            continue
        times_ran += 1
    return dict_fixed
        

def upgrade(upgrade_wanted, cash, number_of_upgrades):
    try:
        if int(upgrade_wanted) not in upgrades.keys():
            if (cash - ((int(upgrade_wanted) * int(number_of_upgrades)) * int(upgrade_wanted) ** 2)) > 0:
                if cash >= (int(upgrade_wanted) * int(number_of_upgrades)) * int(upgrade_wanted) ** 2:
                    upgrades[int(upgrade_wanted)] = int(number_of_upgrades)
                    cash -= (int(upgrade_wanted) * int(number_of_upgrades)) * int(upgrade_wanted) ** 2
                    return cash
            else:
                print(f"To little cash you needed {(int(upgrade_wanted) * int(number_of_upgrades)) * int(upgrade_wanted) ** 2}$ and you have {cash}$")
                return cash
        else:
            if (cash - ((int(upgrade_wanted) * int(number_of_upgrades)) * int(upgrade_wanted) ** 2)) > 0:
                upgrades[int(upgrade_wanted)] += int(number_of_upgrades)
                cash -= (int(upgrade_wanted) * int(number_of_upgrades)) * int(upgrade_wanted) ** 2
                return cash
            else:
                print(f"To little cash you needed {(int(upgrade_wanted) * int(number_of_upgrades)) * int(upgrade_wanted) ** 2}$ and you have {cash}$")
                return cash
    except ValueError:
        pass


def gain_cash(cash, all_upgrade):
    for i in all_upgrade.keys():
        cash += ((1.6**int(i)) * int(all_upgrade[int(i)])) / 5
    return (cash)

def offline_cash_gain(upgrades, time_since_last_played):
    cash = gain_cash(0, upgrades) * time_since_last_played
    return cash

if save_data != "":
    data = saveString_decompile(save_data)
    print(data)
    data[0] = upgrades_decompile(str(data[0]))
    print(data)
    upgrades = data[0]
    print(data[2])
    cash = data[1] + offline_cash_gain(upgrades, data[2])
    print("done")
    

while True:
    try:
        cash = gain_cash(cash, dict(upgrades))
        time.sleep(0.5)
        print(round(cash, 3), "$", end="\n")
    except KeyboardInterrupt:
        print("\n", upgrades)
        try:
            q = input("Enter the upgrade you want to buy as an intager and the number of said upgrades you want to buy format -> [# #]: ")
        except ValueError:
            print("Value must be 2 intagers.")
            continue
        except:
            x = [upgrades, cash, time.time()]
            print("\n", x)
            exit()
        q_split = q.split()
        cash = upgrade(q_split[0], cash, q_split[1])
        print(round(cash, 3))
