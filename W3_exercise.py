import random


meal_price = float(input('How much did the meal cost? '))

discount_choice = input('Do you have a discount? y/n ')
discount_applicable = discount_choice == 'y'

if meal_price > 20 and discount_applicable:
    meal_price = meal_price * 0.9
    print("Discount Applied")
else:
    print("No Discount")

print("Total cost:{}".format(meal_price))
##
temp = float(input("What temp will you set to cook a pizza?"))

if temp > 200:
    print("The oven is too hot")
elif temp < 150:
    print("The oven is too cold")
elif temp == 180:
    print("The oven is at the perfect temp")
else:
    print("The temp is close enough!")

