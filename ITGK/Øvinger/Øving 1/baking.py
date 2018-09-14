su = 400/48
sm = 320/48
sj = 500/48
egg = 2/48
mel = 460/48


def easyBake():
    cookies = int(input("Hvor mange kjeks skal du ha deg?"))

    print("Antall cookies:", round(cookies, 1))
    print("sukker(g):", round(su*cookies, 1))
    print("smør(g):", round(sm*cookies, 1))
    print("sjokolade(g):", round(sj*cookies, 1))
    print("egg:", round(egg*cookies, 1))
    print("hvetemel(g):", round(mel*cookies, 1))


def notEasyBake():
    c1 = int(input("Hvor mange kjeks skal du ha deg?"))
    c2 = int(input("Hvor mange kjeks skal du ha deg?"))
    c3 = int(input("Hvor mange kjeks skal du ha deg?"))

    print("Cookies:\tsukker(g):\tsjokolade(g):")

    cStr = str(c1).rjust(8)
    suStr = str(round(su*c1, 0)).rjust(10)
    sjStr = str(round(sj*c1, 0)).rjust(13)

    print(cStr + "\t" + suStr + "\t" + sjStr)

    cStr = str(c2).rjust(8)
    suStr = str(round(su*c2, 0)).rjust(10)
    sjStr = str(round(sj*c2, 0)).rjust(13)

    print(cStr + "\t" + suStr + "\t" + sjStr)

    cStr = str(c3).rjust(8)
    suStr = str(round(su*c3, 0)).rjust(10)
    sjStr = str(round(sj*c3, 0)).rjust(13)

    print(cStr + "\t" + suStr + "\t" + sjStr)

easyBake()
input()
