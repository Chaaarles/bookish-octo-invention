# a)

# Kodesnutt 1:


def cupcakes():
    cupcakes = 24
    print("Jeg har laget", cupcakes, "cupcakes")


def cakes():
    # Denne funksjonen krasjet pga "cake" defineres etter den skal printes
    print("Men jeg har bare bakt", cake, "kake")
    cake = 1

cupcakes()
cakes()


# Kodesnutt 2:


def cupcakes():
    cupcake = 1
    print("Jeg har laget", cupcake, "cupcake")


def cakes():
    # Denne funksjonen krasjet pga "cupcake" ikke er definert i funksjonen
    print("Og jeg har bakt", cupcake, "kake")

cupcakes()
cakes()


# Kodesnutt 3:


def cupcakes():
    cupcakes = 24
    print("Jeg har laget", cupcakes, "cupcakes")


def cakes():
    print("Men jeg har bare bakt", cake, "kake")

# Denne snutten kjører fordi "cakes()" ikke kjøres
cupcakes()


# b)


def div(x, y):
    num = x / y
    return x, y, num


def pow(x):
    num = x**2
    return x, num


# c)
# Det er ikke et problem fordi num er lokalt i begge tilfellene
