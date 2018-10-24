# a)


def fourth(s):
    return s[::4]

print(fourth("hei sjef hvordan går det? hva skjer nå?"))

# b)


def last2(a):
    out = ""
    for s in a:
        out += s[-2:]
    return out

print(last2(["sabel", "kan", "mestr", "kuleis"]))

# c)
# 1) Man kan ikke mutere strengen direkte
# 2) Denne er rett
# 3) Man kan ikke putte tomme klammeparanteser bak streng :(
