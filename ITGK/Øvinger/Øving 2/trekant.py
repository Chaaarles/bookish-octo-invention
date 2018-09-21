import time
from turtle import *
# importerer funksjoner fra turtle
print("Hei, jeg kan tegne en trekant")
direction = input("Skal trekanten peke opp eller ned? (O/N): ").upper()
if direction == "O":
    rot = 120
elif direction == "N":
    rot = -120

penn = input("Velg en pennefarge, NTNU-rosa (R) eller NTNU-turkis (T): ").upper()
if penn == "R":
    pencolor("#ad208e")
elif penn == "T":
    pencolor("#5CBEC9")

fyll = input("Velg en fyllfarge, NTNU-gul (G), NTNU-oransje (O) elelr NTNU-lilla (L)").upper()
if fyll == "G":
    fillcolor("#d5d10e")
elif fyll == "O":
    fillcolor("#f58025")
elif fyll == "L":
    fillcolor("#552988")        

pensize(7)          # sett pennen 7 piksler tykk
bgcolor("grey")     # sett bakgrunnsfargen graa
# Tegner en fylt trekant
begin_fill()
forward(200)        # gaa 100 piksler framover
left(rot)           # drei 120 grader venstre
forward(200)  
left(rot) 
forward(200)
end_fill()
  
# Holder vinduet med tegningen aapent i 10 sekunder. Ha dette som siste linje i koden din
time.sleep(4)