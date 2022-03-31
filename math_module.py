import math

print(math.pow(2,4))

list_of_people = ["George", "Brenda", "Phillip"]
for person in list_of_people : {
    print(person)
}

for number in range(5):
    print("The next number is : {}".format(number))

new_char =''
for char in "codeFirstGirls":
    new_char = new_char + char + '-'
result = new_char.rstrip('-')
print(result)