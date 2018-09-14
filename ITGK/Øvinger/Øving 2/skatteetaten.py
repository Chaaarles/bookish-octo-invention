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
    print("Dette programmet besvarer om din utleie av fritidsbolig er skattepliktig.")
    print("Først trenger vi å vite om fritidsboligen(e) primært brukes til utleie eller fritid.")
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
        print("Inntekten er skattepliktig")
        if formål == "fritid":
            inntekt -= 10000
            print("Overskytende beløp pr. fritidsbolig er", inntekt)
            inntekt *= 0.85
            print("Skattepliktig inntekt pr fritidsbolig er", inntekt)
        else:
            print("Skattepliktig inntekt pr fritidsbolig er", inntekt)
        print("Totalt skatteplikltig beløp er", inntekt * antall)
        print
    else:
        print("Inntekten er ikke skattepliktig")
        

def sekundær():
    print("INFO")  # Info
    print("Dette programmet besvarer om din utleie av sekundærbolig er skattepliktig.")
    print("Først trenger vi å vite hvor mange sekundærboliger du leier ut.")
    print("Deretter trenger vi å vite hvor store utleieinntekter du har pr. sekundærbolig.")
    linje()

    print("DATAINNHENTING")  # Datainnhenting
    antall = int(input("Skriv inn antallet sekundærboliger du leier ut: "))
    inntekt = int(input("Skriv inn utleieinntekten pr. sekundærbolig: "))
    linje()

    print("SKATTEBEREGNING")  # Skatteberegning
    print("Inntekten er skattepliktig") 
    print("Skattepliktig inntekt pr sekundærbolig er", inntekt)
    print("Totalt skatteplikltig beløp er", inntekt * antall)
    print
        
def valg():
    print("INFO")  # Info
    print("Velkommen til denne skattekalkulatoren!")
    print("Her kan du finne ut om dine leieinntekter på diverse boliger er skattepliktige.")
    print("Først trenger vi å vite hvilken type bolig du har leid ut.")
    linje()

    print("DATAINNHENTING")  # Datainnhenting
    valg = input("Hvilke boligtype vil du kalkulere? (primær/sekundær/fritid): ").lower()
    linje()

    if valg == "primær":
        primær()
    elif valg == "sekundær":
        sekundær()
    else:
        fritid()

valg()
