# a)


def stringos(s1="Hello", s2="world!"):
    return s1 + " " + s2

print(stringos())
print(stringos("James", "Bond"))

# b)


def array1(a):
    string = ""
    for s in a:
        string += s
    return string

print(array1(["a", "b", "c"]))

# c)


def array2(a):
    for s in a:
        print(s[0])

array2(["UKA", "lever", "videre"])

# d)
# "bobbob"
