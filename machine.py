import json

with open("prices.json", "r", encoding="utf-8") as jf:
    prices = json.load(jf)

def display_menu(menu):
    print("Jaki rodzaj biletu chcesz kupić?")
    options = list(menu.keys())
    for index, option in enumerate(options):
        print(f"{index} - {option}")

    try:
        choice = input("Wybór: ")
    except TypeError:
        print("Wprowadzono niepoprawny numer.")
    if choice > len(options)-1 or choice < 0:
        raise ValueError("Wprowadzono niepoprawny typ wartości")
    menu = menu[option[choice]]
    if isinstance(menu, dict):
        return display_menu(menu)
    else:
        return (options[choice], menu)
print(display_menu(prices))




#print("Jaką opcję biletu chcesz kupić?")

#options = list(prices[options[choice]].keys())
#for index, option in enumerate(options):
 #   print(f"{index} - {option}")

#try:
  #  choice = input("Wybór: ")
 #   choice = int(choice)
#except ValueError:
  #  print("Wprowadzono niepoprawny numer opcji.")
 #   exit()

#if choice < 0 or choice >= len(options):
 #   print("Wprowadzono błędny numer opcji.")
#    exit()