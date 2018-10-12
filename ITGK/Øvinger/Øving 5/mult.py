def faktor(i):
    return (1 + 1/pow(i, 2))


def finnI(tol):
    prod = 2
    prodPrev = 0
    i = 1
    while prod - prodPrev > tol:
        i += 1
        prodPrev = prod
        prod = prod * faktor(i)
    return prod, i


def finnR(tol, ti, tprod):
    r = 1
    prod = tprod
    i = ti
    if faktor(i) < 1 + tol:
        return prod, r
    else:
        print("rekursjon")
        prod = prod * faktor(i)
        r += 1
        finnR(tol, i+1, prod)

prod, i = finnI(0.01)
print("Produkt:", round(prod, 2))
print("Rekursjon:", i)
