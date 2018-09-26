# a)
r = 0.5
n = 4
sum = 0
for i in range(n+1):
    sum += r**(i)

print("Summen av rekken er", sum)

# b & c)
tol = 0.001
limit = 2
sum = 0
i = 0
while limit - sum > tol:
    sum += r**i
    i += 1

print("For å være innenfor toleransegrensen:", tol,
      "kjørte løkken", i, "ganger")
print("Differansen mellom virkelig og estimert verdi var da", limit - sum)
