def absolute_values(val):
    return [abs(num) for num in val]


values = [float(n) for n in input().split()]
print(absolute_values(values))