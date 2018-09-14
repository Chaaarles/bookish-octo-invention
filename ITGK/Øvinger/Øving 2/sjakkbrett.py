pos = input("Posisjon: ")
letter = pos[0].upper()
number = int(pos[1])

if letter == ("A" or "C" or "E" or "G"):
    if number % 2 == 0:
        print("Hvit")
    else:
        print("Svart")

elif number % 2 == 0:
    print("Svart")
else:
    print("Hvit")
