from collections import deque

textiles = deque([int(x) for x in input().split()])
medicaments = deque([int(x) for x in input().split()])

healing_items = {"Patch": 0, "Bandage": 0, "MedKit": 0}

while textiles and medicaments:
    textile = textiles.popleft()
    medicament = medicaments.pop()
    if textile + medicament == 30:
        healing_items["Patch"] += 1
    elif textile + medicament == 40:
        healing_items["Bandage"] += 1
    elif textile + medicament >= 100:
        healing_items["MedKit"] += 1
        next_el_resources = (textile + medicament) - 100
        if next_el_resources > 0:
            medicaments[-1] += next_el_resources
    else:
        medicament += 10
        medicaments.append(medicament)


if not medicaments and not textiles:
    print("Textiles and medicaments are both empty.")
elif not medicaments:
    print("Medicaments are empty.")
elif not textiles:
    print("Textiles are empty.")

sorted_items = sorted(healing_items.items(), key=lambda x: (-x[1], x[0]))

while sorted_items[-1][1] == 0:
    sorted_items.pop()
for i in sorted_items:
    print(i[0], "-", i[1])

if medicaments:
    print(f"Medicaments left: {', '.join([str(x) for x in medicaments][::-1])}")
if textiles:
    print(f"Textiles left: {', '.join([str(x) for x in textiles])}")
