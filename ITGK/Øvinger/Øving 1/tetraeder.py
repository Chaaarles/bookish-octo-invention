import math


def tetraeder(h):
    a = 3 * h * (1/math.sqrt(6))
    areal = math.sqrt(3)*math.pow(a, 2)
    volum = math.sqrt(2) * a**3 * (1/12)
    print("Ditt favorittetraeder har areal", areal, "og volum", volum)

h = int(input("Hvor høy er ditt favorittetraeder?"))
tetraeder(h)

input()
