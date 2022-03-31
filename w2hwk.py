import turtle

for number in range(100):
    output = 'o' * number
print(output)

#will print o 99 times


def calculate_vat(amount):
    amount * 1.2

total = calculate_vat(100)
print(total)

#return missing

def build_house():
    side_length = 100
    angle = 120
    turtle.forward(side_length)
    turtle.left(angle)
    turtle.forward(side_length)
    turtle.left(angle)
    turtle.forward(side_length)
    turtle.left(angle)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.done()

build_house()



