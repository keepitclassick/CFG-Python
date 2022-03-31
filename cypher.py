def encode_char(char):
    return 'axzc' + char + 'djap'

def cipher():
    word = input("Please enter the word to encode.")
    encoded = ''

    for char in word:
        encoded += encode_char(char)

    return encoded

print(cipher())

for number in range(100):
    output = 'o' * number
print(output)