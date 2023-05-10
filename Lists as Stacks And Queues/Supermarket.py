# people = []
# while True:
#     name = input()
#     if name == "End":
#         print(f"{len(people)} people remaining.")
#         break
#
#     if name != "Paid":
#         people.append(name)
#     else:
#         print("\n".join(people))
#         people.clear()
#

from _collections import deque

names_deque = deque()
COMMAND_END = "End"
COMMAND_PAID= "Paid"

while True:
    command = input()

    if command == COMMAND_END:
        print(f"{len(names_deque)} people remaining.")
        break
    elif command == COMMAND_PAID:
        while names_deque:
            print(names_deque.popleft())

    else:
        names_deque.append(command)