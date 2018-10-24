# a)


def stripper(s):
    s = s.strip()
    s = s.upper()
    return s

print(stripper(" \n  The Sky's Awake So I'm Awake  \t  "))

# b)


def splitterino(s, c):
    return s.split(c)

print(splitterino("Hakuna Matata", "a"))

# c)
# "My bed is a magical place where I suddenly
# remember everything I forgot to do."

# d)


def z(c="Z"):
    for i in range(7):
        print((i+1)*c)
    for i in range(8):
        print((8-i)*c)

z()
z("Aa")
