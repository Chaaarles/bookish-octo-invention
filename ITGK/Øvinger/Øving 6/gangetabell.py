# a)


def separate(numbers, threshold):
    less_than = []
    more_than = []
    for x in numbers:
        if x < threshold:
            less_than.append(x)
        else:
            more_than.append(x)
    return less_than, more_than

less_than, more_than = separate([1, 2, 3, 4, 5], 3)
print(less_than)
print(more_than)


# b)


def multiplication_table(n):
    table = []
    for y in range(1, n+1):
        row = []
        for x in range(1, n+1):
            row.append(x*y)
        table.append(row)
    return table

print(multiplication_table(6))
