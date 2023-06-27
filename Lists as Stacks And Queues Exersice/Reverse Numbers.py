# numbers = input().split()
# for num in range(len(numbers)):
#     print(f"{numbers.pop()}", end=" ")
#
#

from collections import deque

text = deque(input().split())
text.reverse()
print(" ".join(text))