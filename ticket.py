class Ticket:
    def init(self, category, ticket_type, option, price):
        self.category = category          
        self.ticket_type = ticket_type    
        self.option = option             
        self.price = price

    def str(self):
        return f"{self.category},  {self.ticket_type}  {self.option}{self.price}" 