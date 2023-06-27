from collections import deque

gas_stations = deque([[int(x) for x in input().split()] for _ in range(int(input()))])
gas_stations_copy = gas_stations.copy()

index = 0
gas_in_tank = 0

while gas_stations_copy:
    petrol, distance = gas_stations_copy.popleft()

    gas_in_tank += petrol

    if gas_in_tank - distance < 0:
        gas_stations.rotate(-1)
        gas_stations_copy = gas_stations.copy()
        index += 1
        gas_in_tank = 0
    else:
        gas_in_tank -= distance

print(index)