sum = 0
for i in range(7):
    sum += int(input("Skriv inn et heltall: "))
print("Summen av tallene ble", sum)

product = 1
factor = 1
while product < 1000:
    product *= factor
    factor += 1
    print(product)

isTrue = False
numGuess = 0
while not isTrue:
    numGuess += 1
    guess = input("Ladies and gentlemen...").upper()
    if guess == "WE GOT HIM":
        print("Nice! Bare", numGuess, "forsøk :O")
        isTrue = True
    else:
        print("ERR!!!!!")
