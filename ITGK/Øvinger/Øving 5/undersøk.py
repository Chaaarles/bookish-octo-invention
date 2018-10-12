from sys import exit

folk = [0, 0]
tarFag = 0
tarITGK = 0
timer = 0


def hade(spm="HADE"):
    if spm.upper() == "HADE":
        print("Antall kvinner", folk[1])
        print("Antall menn", folk[0])
        print("Antall tar fag", tarFag)
        print("Antall tar ITGK", tarITGK)
        print("Antall timer på lekser", timer/tarFag)
        exit()


def sjekk_jn(spm):
    if spm.upper() == "J":
        return 1
    elif spm.upper() == "N":
        return 0


def sjekk_kjonn(kjonn):
    hade(kjonn)

    if kjonn.upper() == "M":
        kjonn = 0
    elif kjonn.upper() == "K":
        kjonn = 1
    else:
        sjekk_kjonn(input("Er du mann eller kvinne? (m/k) "))
    return kjonn


def sjekk_alder(alder):
    hade(alder)

    alder = int(alder)

    if not (alder > 16 and alder < 26):
        print("Du kan ikke ta undersøkelsen")
        return False
    return alder


def sjekk_fag(spm):
    hade(spm)

    jn = sjekk_jn(spm)

    if jn == 0 or jn == 1:
        return jn
    else:
        sjekk_fag(input("Tar du et fag? (j/n) "))


def sjekk_ITGK(spm):
    hade(spm)

    jn = sjekk_jn(spm)

    if jn == 0 or jn == 1:
        return jn
    else:
        sjekk_fag(input("Tar du ITGK? (j/n) "))


def sjekk_timer(spm):
    hade(spm)

    return int(spm)


def test():
    global folk
    global tarFag
    global tarITGK
    global timer

    while True:
        print("Velkommen til spørreundersøkelse!")

        kjonn = sjekk_kjonn(input("Er du mann eller kvinne? (m/k) "))
        alder = sjekk_alder(input("Hvor gammel er du? "))
        if not alder:
            continue

        folk[kjonn] += 1

        fag = sjekk_fag(input("Tar du et fag? (j/n) "))
        if fag == 0:
            continue
        if alder > 22:
            ITGK = sjekk_ITGK(input("Tar du virkelig ITGK? (j/n) "))
        else:
            ITGK = sjekk_ITGK(input("Tar du ITGK? (j/n) "))
        tid = sjekk_timer(
            input("Hvor mange timer bruker du på lekser daglig? "))

        tarFag += 1
        tarITGK += ITGK
        timer += tid

test()

# Man vil kunne lese svarene som er skrevet inn i terminalen, men man kan ikke
# hente dem ut fra noe annet sted ettersom verdiene bare var lagret i
# arbeidsminnet.
