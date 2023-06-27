from collections import deque

elves = deque([int(x) for x in input().split()])
materials = deque([int(x) for x in input().split()])

total_toys = 0
counter = 0
total_elves_energy = 0

while materials and elves:
    while elves[0] < 5:
        elves.popleft()
        if len(elves) == 0:
            break
    if len(elves) == 0:
        break

    counter += 1
    if counter % 3 != 0:
        if elves[0] >= materials[-1]:
            if counter % 5 == 0:
                elves[0] -= materials[-1]
            else:
                total_toys += 1
                elves[0] = (elves[0] - materials[-1]) + 1  # NEW ENERGY WITH COOKIE
            total_elves_energy += materials[-1]  # ADD TO TOTAL ENERGY
            elves.append(elves.popleft())
            materials.pop()     # REMOVE USED MATERIALS FROM DEQUE
        else:               # IF ELF DOES NOT HAVE ENOUGH ENERGY
            elves[0] *= 2
            elves.append(elves.popleft())

    elif counter % 3 == 0:
        if elves[0] >= materials[-1]*2:
            if counter % 5 == 0:
                elves[0] -= materials[-1]*2
            else:
                total_toys += 2
                elves[0] = (elves[0] - materials[-1]*2) + 1  # NEW ENERGY WITH COOKIE
            total_elves_energy += materials[-1]*2  # ADD TO TOTAL ENERGY
            elves.append(elves.popleft())
            materials.pop()     # REMOVE USED MATERIALS FROM DEQUE
        else:       # IF ELF DOES NOT HAVE ENOUGH ENERGY
            elves[0] *= 2
            elves.append(elves.popleft())


print(f"Toys: {total_toys}")
print(f"Energy: {total_elves_energy}")
if elves:
    print(f"Elves left: {', '.join([str(x) for x in elves])}")
if materials:
    print(f"Boxes left: {', '.join([str(x) for x in materials])}")
