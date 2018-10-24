def coinageForTeeth(teeth):
    coins = []
    for tooth in teeth:
        theseCoins = [0, 0, 0, 0]
        while tooth > 0:
            if tooth >= 20:
                theseCoins[0] += 1
                tooth -= 20
            elif tooth >= 10:
                theseCoins[1] += 1
                tooth -= 10
            elif tooth >= 5:
                theseCoins[2] += 1
                tooth -= 5
            else:
                theseCoins[3] += 1
                tooth -= 1
        coins.append(theseCoins)
    return coins

teeth = [95, 103, 71, 99, 114, 64, 95, 53, 97, 114, 109, 11, 2, 21, 45, 2, 26,
         81, 54, 14, 118, 108, 117, 27, 115, 43, 70, 58, 107]

print(coinageForTeeth(teeth))
