from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money=MoneyMachine()
coffee=CoffeeMaker()
items=Menu()
is_on=True
while is_on:
 user_input = input("What would you like? (espresso/latte/cappuccino/):")
 if user_input=="report":
  print(coffee.resources)
 elif user_input=="off":
  is_on=False
 else:
  drink = items.find_drink(user_input)
  a=coffee.is_resource_sufficient(drink)

  if a:
   if(money.make_payment(drink.cost)):
      coffee.make_coffee(drink)


