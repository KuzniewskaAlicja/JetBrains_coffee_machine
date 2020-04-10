from coffee_machine.machine import *

if __name__ == '__main__':
    coffee_machine = CoffeeMachine(400, 100, 20, 15, 550)
    coffee_machine.run_machine()