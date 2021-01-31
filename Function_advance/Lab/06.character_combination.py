from itertools import permutations

text = [el for el in input()]

[print(''.join(el)) for el in permutations(text)]