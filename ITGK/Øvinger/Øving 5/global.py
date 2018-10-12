# Del A
import math

GRAVITY = 9.81


def get_fall_time(m):
    global GRAVITY

    t = math.sqrt((2 * m) / GRAVITY)
    print("Det tar", t, "sekunder å ramle", m, "meter")

get_fall_time(int(input("Meter: ")))


# Del B


def set_gravity(gravity):
    global GRAVITY
    GRAVITY = gravity


def get_fall_time(m, gravity=GRAVITY):
    t = math.sqrt((2 * m) / gravity)
    print("Det tar", t, "sekunder å ramle", m, "meter")


# I denne situasjonen er funksjonene så enkle at det ikke er hensiktsmessig å
# lage en egen funksjon for å sette GRAVITY

# Derimot vil det i et større og mer komplekst system være greit å kunne
# redefinere globale variabler i stedet for å bruke ekstra parameter i
# funksjonene
