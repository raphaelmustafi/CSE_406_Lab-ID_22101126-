# FCFS Disk Scheduling

# request sequence from user
requests = list(map(int, input("Enter request sequence (space separated): ").split()))

# head position from user
head = int(input("Enter initial head position: "))

total_seek = 0
current = head
path = [head]

for req in requests:
    distance = abs(req - current)
    total_seek += distance
    current = req
    path.append(current)

print("Head Movement Path:", " -> ".join(map(str, path)))
print("Total Seek Operations:", total_seek)
