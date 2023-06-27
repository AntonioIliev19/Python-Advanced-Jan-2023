# occ = {}
#
# for letter in input():
#     occ[letter] = occ.get(letter, 0) + 1
#     # if letter not in occ:
#     #     occ[letter] = 0
#     # occ[letter] += 1
#
# for letter, time in sorted(occ.items()):
#     print(f"{letter}: {time} time/s")

text = input()

for letter in sorted(set(text)):
    print(f"{letter}: {text.count(letter)} time/s")