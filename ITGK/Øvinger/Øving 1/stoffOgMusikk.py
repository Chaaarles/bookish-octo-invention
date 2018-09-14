def stoff():
    stoff = input("Hvilket stoff er du i besittelse av? ")
    molvekt = input("Hva er molvekt for " + stoff + "? ")
    gram = input("Hvor mange gram " + stoff + "er du i besittelse av? ")
    molekyler = float(gram) / float(molvekt) * 6.022e23
    print("Du er i besittelse av", format(
        molekyler, '.2e'), stoff + "molekyler!")


def melodi():
    dineLinjer = int(input("Hvor mange 10-toners melodilinjer har du hørt?"))
    linjeProsent = format(dineLinjer/8.25e19, '.2e')
    print("Du har hørt", linjeProsent + "% av alle 10-toners melodilinjer")


funksjon = input("Hvilken funksjon? | (S)toff/(M)elodi ").upper()

if funksjon == "S" or funksjon == "STOFF":
    stoff()
elif funksjon == "M" or funksjon == "MELODI":
    melodi()

input()
