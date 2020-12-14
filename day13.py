import sys

input_file = sys.argv[1]
with open(input_file, "r") as file:
    data = file.readlines()
    earliest_time = int(data[0])
    departures = []
    for i, bus in enumerate(data[1].split(",")):
        if bus != "x":
            departures.append((i, int(bus)))

    bus_ids = [int(i) for i in data[1].split(",") if i != "x"]

wait_time = [earliest_time % i - i for i in bus_ids]
bus_id = bus_ids[wait_time.index(max(wait_time))]
print(bus_id * -max(wait_time))

time, step = 0, 1

for offset, bus_id in departures:
    while (time + offset) % bus_id:
        time += step
    step *= bus_id

print(time)