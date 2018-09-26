k = int(input("Skriv inn et heltall: "))
this = 0
prev = 0
sum = 0
for i in range(k+1):
    if i == 0:
        this = 0
    if i == 1:
        prev = 0
        this = 1
    else:
        temp = this
        this += prev
        prev = temp
    print(this)
    sum += this
print("Summen av tallene er", sum)
