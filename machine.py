from cart import Cart
from payment import Payment_method
from ticket import Ticket
import json
import re


class TicketMachine:
    def __init__(self):
        self.cart = []
        with open("prices.json", "r", encoding="UTF-8") as jf:
            self.prices = json.load(jf)

    def display_menu(self, menu=None):
        if menu is None:
            menu = self.prices

        print("Jaką opcję biletu chcesz kupić?")
        options = list(menu.keys())
        for index, option in enumerate(options):
            print(f"{index} - {option}")

        try:
            choice = int(input("Wybór: "))
        except ValueError:
            print("Wprowadzono niepoprawny typ wartości.")
            return self.display_menu(menu)

        if choice > len(options) - 1 or choice < 0:
            print("Wprowadzono błędny numer opcji.")
            return self.display_menu(menu)

        selected_option = menu[options[choice]]

        if isinstance(selected_option, dict):
            return self.display_menu(selected_option)
        else:
            ticket_name = options[choice]
            price = selected_option
            return Ticket(ticket_name, price)

    def register_payment(self):
        total = sum(ticket.price for ticket in self.cart)
        print(f"Kwota do zapłaty: {total} zł")
        payment_method = input("Wybierz metodę płatności:\n b - BLIK\n k - karta\n g - gotówka\n")

        if payment_method.lower() == 'b':
            blik = input("Podaj kod BLIK: ")
            if re.fullmatch(r"\d{6}", blik):
                print("Transakcja się powiodła")
            else:
                decision = input("Podano niepoprawny kod. Czy chcesz spróbować jeszcze raz (t/n)? ")
                if decision.lower() == 't':
                    self.register_payment()
                else:
                    exit()

        elif payment_method.lower() == 'k':
            print("Proszę zbliżyć kartę do czytnika...")
            input("Potwierdź transakcję: ")
            print("Transakcja się powiodła")

        elif payment_method.lower() == 'g':
            paid = 0
            while paid < total:
                try:
                    paid += float(input("Wprowadź gotówkę: "))
                except ValueError:
                    print("Niepoprawna wartość.")
                    continue

                if paid < total:
                    decision = input("Wprowadzono za mało gotówki. Czy chcesz dopłacić (t/n)? ")
                    if decision.lower() != 't':
                        exit()
            change = round(paid - total, 2)
            if change > 0:
                print(f"Reszta: {change} zł")

        else:
            decision = input("Wybrano niepoprawną opcję. Czy chcesz spróbować jeszcze raz (t/n)? ")
            if decision.lower() == 't':
                self.register_payment()
            else:
                exit()

    def display_cart(self):
        for ticket in self.cart:
            print(f"Bilet: {ticket.name}\tCena: {ticket.price} zł")
