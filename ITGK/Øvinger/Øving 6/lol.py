# a)
number_list = [i for i in range(100)]
print(number_list)


# b)
sum = 0
for x in range(100):
    if (x % 3) == 0 or (x % 10) == 0:
        sum += x
print(sum)


# c)
def byttPlass(numbers):
    for i in range(0, len(numbers), 2):
        temp = numbers[i]
        numbers[i] = numbers[i+1]
        numbers[i+1] = temp

byttPlass(number_list)
print(number_list)


# d)
reversed_list = []
for i in range(1, len(number_list) + 1):
    reversed_list.append(number_list[-i])

print(reversed_list)
