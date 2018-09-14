primAndel = 0
primInntekt = 0


def linje():
    print("---------------------------------------" +
          "-------------------------------")


def primær():
    print("INFO:")  # Info
    print("Dette programmet besvarer om din utleie av egen" +
          "bolig er skattepliktig.")
    print("Først trenger vi å vite hvor stor del av boligen du har leid ut.")
    print("Angi dette i prosent, 100 betyr hele boligen, 50 betyr halve,")
    print("20 en mindre del av boligen som f.eks. en hybel.")
    linje()

    print("DATAINNHENTING:")  # Datainnhenting
    global primAndel
    global primInntekt
    primAndel = int(input("Oppgi hvor mye av boligen som ble utleid: "))
    primInntekt = int(input("Skriv inn hva du har hatt i leieinntekt: "))
    linje()

    print("SKATTEBEREGNING")  # Skatteberegning
    if primAndel < 50 or primInntekt < 20000:
        print("Inntekten er ikke skattepliktig")
    else:
        print("Inntekten er skattepliktig")
        print("Skattepliktig beløp er", primInntekt)


def fritid():
    print("INFO")  # Info
    print("Dette programmet besvarer om din utleie en annen type bolig,")
    print("her fritidsbolig, er skattepliktig.")
    print("Vi trenger vi først å vite om fritidsboligen(e) primært brukes til utleie eller fritid.")
    print("Deretter trenger vi å vite hvor mange fritidsboliger du leier ut.")
    print("Til slutt trenger vi å vite hvor store utleieinntekter du har pr. fritidsbolig.")
    linje()

    print("DATAINNHENTING")  # Datainnhenting
    formål = input("Skriv inn formålet med fritidsboligen(e) (fritid/utleie): ").lower()
    antall = int(input("Skriv inn antallet fritidsboliger du leier ut: "))
    inntekt = int(input("Skriv inn utleieinntekten pr. fritidsbolig: "))
    linje()

    print("SKATTEBEREGNING")  # Skatteberegning
    if formål == "utleie" or inntekt > 10000:
        if formål == "utleie":
            rabatt = 10000
        print("Inntekten er skattepliktig")
        if formål == :
            pass
        print
        