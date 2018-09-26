word = input("Skriv inn det hemmelige ordet: ").upper()
chars = {}
for char in word:
    chars[char] = False
lives = int(input("Hvor mange forsøk har brukeren? "))

game = True
correct = 0

while game:
    hint = ""
    for char in word:
        if(chars[char]):
            hint += char
        else:
            hint = hint + "*"
    print(hint)
    guess = input("Gjett på én bokstav i ordet: ").upper()
    if guess in chars and not chars[guess]:
        chars[guess] = True
        print("Big nice!")
        correct += 1
    else:
        lives -= 1
        print("Big oofs left:", lives)

    if lives < 1:
        print("You just fricking lost you fricking frick!")
        game = False
    elif correct == len(chars):
        print("Ladies and gentlemen, we got him!", word)
        game = False
