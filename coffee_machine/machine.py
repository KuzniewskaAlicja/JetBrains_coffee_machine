from coffee_machine.product_config import *

class CoffeeMachine:
    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money
        self.coffee_type = None
        self.action = None
    
    def remained_resources(self):
        print(f'The coffee machine has:\n\
                {self.water} of water\n\
                {self.milk} of milk\n\
                {self.beans} of coffee beans\n\
                {self.cups} of disposable cups\n\
                ${self.money} of money')

    def get_action(self):
        self.action = input('Write action (buy, fill, take, remaining, exit)\n')
    
    def get_coffee_type(self):
        self.coffee_type = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back:\n')
    
    def make_coffee(self):
        resources_need = tuple()
        if self.coffee_type == '1':
            resources_need = ESPRESSO
        elif self.coffee_type == '2':
            resources_need = LATTE
        elif self.coffee_type == '3':
            resources_need = CAPPUCCINO
        else:
            print('We haven"t that type of coffee')
        
        if self.checking_resources(resources_need):
            self.water -= resources_need.get('water', 0)
            self.milk -= resources_need.get('milk', 0)
            self.beans -= resources_need.get('coffee_beans', 0)
            self.money += resources_need.get('cost', 0)
            self.cups -= 1
        else:
            if self.water < resources_need.get('water'):
                print('Sorry, not enough water!')
            elif self.milk < resources_need.get('milk'):
                print('Sorry, not enough milk!')
            elif self.beans < resources_need.get('coffee_beans'):
                print('Sorry, not enough coffee beans!')

    def checking_resources(self, resources_need):
        if (self.water > resources_need.get('water') and
            self.milk > resources_need.get('milk') and
            self.beans > resources_need.get('coffee_beans')):
            print('I have enough resources, making you a coffee!')
            return True
        else:
            return False

    def fill(self):
        self.water += int(input('Write how many ml of water do you want to add:\n'))
        self.milk += int(input('Write how many ml of milk do you want to add:\n'))
        self.beans += int(input('Write how many grams of coffee beans do you want to add:\n'))
        self.cups += int(input('Write how many disposable cups of coffee do you want to add:\n'))
    
    def take_money(self):
        print(f'I gave you ${self.money}')
        self.money = 0
    
    def run_machine(self):
        while True:
            self.get_action()
            if self.action == 'buy':
                self.get_coffee_type()
                if self.coffee_type != 'back':
                    self.make_coffee()
                else:
                    continue
            elif self.action == 'fill':
                self.fill()
            elif self.action == 'take':
                self.take_money()
            elif self.action == 'remaining':
                self.remained_resources()
            elif self.action == 'exit':
                break
            else:
                print(f'Unable to perform {self.action}')