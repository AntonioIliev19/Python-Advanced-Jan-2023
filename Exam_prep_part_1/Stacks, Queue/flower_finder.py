from collections import deque


def check_word(char, word):
    if char in word:
        word = word.replace(char, "")
    return word


vowels = deque(input().split())
consonants = deque(input().split())

found_word = False
flowers = ["rose", "tulip", "lotus", "daffodil"]

while vowels and consonants:
    vowel = vowels.popleft()
    consonant = consonants.pop()
    for idx in range(len(flowers)):
        flowers[idx] = check_word(vowel, flowers[idx])
        if flowers[idx] == "":
            found_word = True
            break
        flowers[idx] = check_word(consonant, flowers[idx])
        if flowers[idx] == "":
            found_word = True
            break
    if found_word:
        break

if not found_word:
    print("Cannot find any word!")
else:
    found_index_word = flowers.index("")
    if found_index_word == 0:
        print(f"Word found: rose")
    if found_index_word == 1:
        print(f"Word found: tulip")
    if found_index_word == 2:
        print(f"Word found: lotus")
    if found_index_word == 3:
        print(f"Word found: daffodil")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
