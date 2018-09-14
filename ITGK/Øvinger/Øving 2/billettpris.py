minipris = 199
fullpris = 440

barn = 0.5
rabatt = 0.75


def pris(billett):
    student = 1
    studentMini = 1
    studentValg = input("Studerer du? (J/N): ").upper()
    if studentValg == "J":
        student = 0.75
        studentMini = 0.9
    if billett == "MINI":
        print("Prisen på din billett blir:", minipris * studentMini)
    else:
        alder = int(input("Skriv inn din alder: "))
        if alder < 16:
            print("Prisen på din billett blir:", fullpris * barn * student)

        elif alder >= 16 and alder < 60:
            militær = input("Er du i militæret? (J/N): ").upper()
            if militær == "J":
                print("Prisen på din billett blir:",
                      fullpris * rabatt * student)
            else:
                print("Prisen på din billett blir:", fullpris * student)
        else:
            print("Prisen på din billett blir:",
                  float(fullpris) * rabatt * student)


dtr = int(input("Dager til du skal reise: "))
if dtr >= 14:
    print("Minipris:", minipris, "kan ikke refunderes/endres.")
    valg = input("Ønskes dette? (J/N): ").upper()
    if valg == "J":
        pris("MINI")
    else:
        pris("FULL")
else:
    pris("FULL")
