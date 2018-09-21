import random
import pygame.mixer
import time
x = random.randint(1,100)
high = 100
low = 1
boole = False

pygame.mixer.init()
gotHim = pygame.mixer.Sound("audio/epicWinTime.ogg")

while boole == False:
    guess = int(input("Make your best guess ("+ str(low) + "/" + str(high) + ") : "))
    
    if guess < x:
        print("I wanna get high, yeah!")
        low = guess
    elif guess > x:
        print("To the windows, to the wall!")
        high = guess
    else:
        boole = True
        print("Ladies and gentlemen..") 
        gotHim.play()
        time.sleep(3)
        print("We got him!")
        time.sleep(8)
