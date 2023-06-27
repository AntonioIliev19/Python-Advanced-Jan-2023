def start_spring(**kwargs):
    flowers, sorted_output = {}, []
    for flower, type_flower in kwargs.items():
        if type_flower not in flowers:
            flowers[type_flower] = []
        flowers[type_flower].append(flower)
    for s_type_flower, s_flower in sorted(flowers.items(), key=lambda x: (-len(x[1]), x[0])):      # s = sorted
        sorted_output.append(f"{s_type_flower}:")
        for value in sorted(s_flower):
            sorted_output.append(f"-{value}")

    return '\n'.join(sorted_output)


example_objects = {"Magnolia": "tree",
 "Swallow": "bird",
"Thrushes": "bird",
"Pear": "tree",
"Cherries": "tree",
"Shrikes": "bird",
"Butterfly": "insect"}
print(start_spring(**example_objects))

