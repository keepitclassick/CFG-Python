chairs = 15
nails = 4
total_nails = chairs * nails
message = 'I need to buy {} nails.'.format(total_nails)
print(message) #this should be changed to message variable and no string

#The program is not calculating correctly because the string and int * will not act as a math operation and instead
# multiply the string
#to fix it remove the '' from chars so it is treated as an integer

my_name = 'Penelope'
my_age = 29
message = 'My name is {} and I am {} years old.'.format(my_name, my_age)
print(message)

#error is Penelope is not defined
#it is treating Penelope as a variable because it doesn't have '' to indicate it is a string

eggs_per_box = 6
boxes_of_eggs = 6
eggs_needed_for_omelette = 4
total_omelettes = eggs_per_box * boxes_of_eggs // eggs_needed_for_omelette

output = "You can make {} omelettes with {} boxes of eggs.".format(total_omelettes, boxes_of_eggs)
print(output)