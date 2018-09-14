from turtle import *
import time
from colour import Color

colormode(255)


def checkColor(col):
    cR = 0
    cG = 0
    cB = 0

    try:
        col = col.replace(" ", "")
        Color(col)

        print(col)
        return col
    except ValueError:
        try:
            col = int(float(col))
            if 0 <= col <= 16777215:
                cR = col // 256 // 256
                cG = col // 256 % 256
                cB = col % 256
                col = (cR, cG, cB)

            print(col)
            return col
        except ValueError:
            print("Nah dude")


# setter opp tegnevinduet
setup(330, 330, 0, 0)
screensize(315, 315)
goto(-60, 150)

# velger farger
bgcolorinput = input("Velg en bakgrunnsfarge (0-16777215 / fargenavn): ")
bgcolor(checkColor(bgcolorinput))

colorInput = input("Velg en farge (0-16777215 / fargenavn): ")
color(checkColor(colorInput))

# tegner den indre firkanten
begin_fill()
right(10)  # tilter den 10 grader nedover
forward(200)
right(90)
forward(200)
right(90)
forward(200)
right(90)
forward(200)
end_fill()

time.sleep(3)  # Holder vinduet åpent i 10 sek
