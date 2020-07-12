class CoffeeMachine:
    item_dict = {'def_water': 400, 'def_milk': 540, 'def_coffee': 120, 'def_cup': 9, 'def_money': 550, 'exit': True}

    def coffee_machine_state(self, water=0, milk=0, coffee=0, cup=0, money=0):
        water += CoffeeMachine.item_dict['def_water']
        milk += CoffeeMachine.item_dict['def_milk']
        coffee += CoffeeMachine.item_dict['def_coffee']
        cup += CoffeeMachine.item_dict['def_cup']
        money += CoffeeMachine.item_dict['def_money']
        CoffeeMachine.item_dict['def_water'] = water
        CoffeeMachine.item_dict['def_milk'] = milk
        CoffeeMachine.item_dict['def_coffee'] = coffee
        CoffeeMachine.item_dict['def_cup'] = cup
        CoffeeMachine.item_dict['def_money'] = money

    def machine_remaining(self):
        water = CoffeeMachine.item_dict['def_water']
        milk = CoffeeMachine.item_dict['def_milk']
        coffee = CoffeeMachine.item_dict['def_coffee']
        cup = CoffeeMachine.item_dict['def_cup']
        money = CoffeeMachine.item_dict['def_money']
        print()
        print('The coffee machine has:')
        print(f'{water} of water')
        print(f'{milk} of milk')
        print(f'{coffee} of coffee beans')
        print(f'{cup} of disposable cups')
        print(f'{money} of money')
        print()

    def buy_coffee(self):
        water = CoffeeMachine.item_dict['def_water']
        milk = CoffeeMachine.item_dict['def_milk']
        coffee = CoffeeMachine.item_dict['def_coffee']
        cup = CoffeeMachine.item_dict['def_cup']
        which_coffee = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
        if which_coffee == '1':
            if water > 250 and coffee > 16 and cup > 1:
                print('I have enough resources, making you a coffee!')
                self.coffee_machine_state(water=-250, coffee=-16, money=4, cup=-1)
            elif water < 250:
                print('Sorry, not enough water!')
            elif coffee < 16:
                print('Sorry, not enough coffee!')
            elif cup < 1:
                print('Sorry, not enough disposable cups!')
        elif which_coffee == '2':
            if water > 350 and coffee > 20 and cup > 1 and milk > 75:
                print('I have enough resources, making you a coffee!')
                self.coffee_machine_state(water=-350, coffee=-20, money=7, milk=-75, cup=-1)
            elif water < 350:
                print('Sorry, not enough water!')
            elif coffee < 20:
                print('Sorry, not enough coffee!')
            elif milk < 75:
                print('Sorry, not enough disposable milk!')
            elif cup < 1:
                print('Sorry, not enough disposable cups!')
        elif which_coffee == '3':
            if water > 200 and coffee > 12 and cup > 1 and milk > 100:
                print('I have enough resources, making you a coffee!')
                self.coffee_machine_state(water=-200, coffee=-12, money=6, milk=-100, cup=-1)
            elif water < 200:
                print('Sorry, not enough water!')
            elif coffee < 12:
                print('Sorry, not enough coffee!')
            elif milk < 100:
                print('Sorry, not enough disposable milk!')
            elif cup < 1:
                print('Sorry, not enough disposable cups!')
        elif which_coffee == 'back':
            print('back')

    def fill_machine(self):
        water = int(input('Write how many ml of water do you want to add:'))
        milk = int(input('Write how many ml of milk do you want to add:'))
        coffee = int(input('Write how many grams of coffee beans do you want to add:'))
        cup = int(input('Write how many disposable cups of coffee do you want to add:'))
        self.coffee_machine_state(water=water, milk=milk, coffee=coffee, cup=cup)

    def take_action(self):
        action = input('Write action (buy, fill, take, remaining, exit)):').lower()
        if action == 'buy':
            self.buy_coffee()
        elif action == 'fill':
            self.fill_machine()
        elif action == 'take':
            take_money = CoffeeMachine.item_dict['def_money']
            print(f'I gave you ${take_money}')
            self.coffee_machine_state(money=-take_money)
        elif action == 'exit':
            self.item_dict['exit'] = False
        elif action == 'remaining':
            self.machine_remaining()
my_coffee_machine = CoffeeMachine()
while CoffeeMachine.item_dict['exit']:
    my_coffee_machine.take_action()

