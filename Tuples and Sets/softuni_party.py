n = int(input())
came = set()

for _ in range(n):
    res_num = input()
    came.add(res_num)


guest_reservation_num = input()
while guest_reservation_num != "END":
    came.remove(guest_reservation_num)
    guest_reservation_num = input()

print(len(came))
for num in sorted(came):
    print(num)
