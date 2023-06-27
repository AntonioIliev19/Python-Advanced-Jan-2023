first_line = set(input().split())
second_line = set(input().split())

first_line_copy = first_line.copy()
second_line_copy = second_line.copy()

for _ in range(int(input())):
    command = input()
    if command == "Check Subset":
        print(first_line.issubset(second_line) or second_line.issubset(first_line))
        continue

    token = command.split()
    for el in token:
        check_num = el.isnumeric()

        if check_num and token[0] == "Add" and token[1] == "First":
            first_line_copy.add(el)
        elif check_num and token[0] == "Add" and token[1] == "Second":
            second_line_copy.add(el)
        elif check_num and token[0] == "Remove" and token[1] == "First":
            second_line_copy.discard(el)
        elif check_num and token[0] == "Remove" and token[1] == "Second":
            second_line_copy.discard(el)

print(', '.join(sorted(first_line_copy)))
print(', '.join(sorted(second_line_copy)))
