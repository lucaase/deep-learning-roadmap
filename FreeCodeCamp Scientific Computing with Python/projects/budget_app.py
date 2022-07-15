class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = list()
        self.balance = 0

    def check_funds(self, amount):
        return amount <= self.balance

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})
        self.balance += amount

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            self.balance -= amount
            return True
        else:
            return False
            

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': 'Transfer to ' + category.name})
            category.ledger.append({'amount': amount, 'description': 'Transfer from ' + self.name})
            return True
        else:
            return False

    def __str__(self):
        header = self.name.center(30, "*") + "\n"
        items = ""
        for item in self.ledger:
            # format description and amount
            line_description = "{:<23}".format(item["description"])
            line_amount = "{:>7.2f}".format(item["amount"])
            # Truncate ledger description and amount to 23 and 7 characters respectively
            items += "{}{}\n".format(line_description[:23], line_amount[:7])
        total = "Total: {:.2f}".format(self.balance)
        return header + items + total
    


def create_spend_chart(categories):
    
    title = 'Percentage spent by category'+ '\n'
    total = 0 
    counts = {} 
    percentage = {}
    name_length = 0   
   

    for category in categories:
        countkey = category.wd_count() 
        counts[category.name] = countkey 
        total += countkey 


    for name, count in counts.items():
        percent = count / total * 100
        percentage[name] = percent
 
   
    x = 100 
    for number in range(11):
        row = f"{x}".rjust(3) + "| "
        for name, percent in percentage.items():
            if percent >= (x):
                row += "o  "
            else:
                row += "   "
        title += row + '\n'
        x -= 10
   
    x_axis = "    -" 
    for category in categories:
        x_axis += ("---")
    title += x_axis + "\n"


    for category in categories:
        if len(category.name) > name_length:
            name_length = len(category.name)
 
    
    y = 0
    while y <= name_length:
        rows = "     "
        for key, value in percentage.items():
            category_name = key
            try:    
                rows +=  category_name[y] + "  "
            except: 
                rows += "   "
        
        if y <= name_length -1:
            title += rows + '\n' 
        else:
            title += rows.strip(" ")
           
        y = y + 1
    title = title.rstrip("\n")
    return title


# Run some tests
food = budget.Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = budget.Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = budget.Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)

print(create_spend_chart([food, clothing, auto]))