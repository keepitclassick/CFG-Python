name = input("Whats your name? ")
print("Hello, {}".format(name))

animal = input("What type of pet is your favourite? ")
pet_name = input("What would you name them? ")
print("You'd like a {} as a pet and would name them {}".format(animal, pet_name))

friends = input("How many friends do you need to feed? ")
pizzas = int(friends) * 0.5

print("You need {} pizzas for to feed your {} friends.".format(pizzas, friends))