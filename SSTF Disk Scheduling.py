# SSTF Disk Scheduling (ID:22101126)

reqs = [int(x) for x in input(" Requests Sequence: ").split()]
head = int(input(" Head: "))

total = 0
seq = []

while reqs:
    nearest = reqs[0]
    for r in reqs:
        if abs(r - head) < abs(nearest - head):  # first find closest request
            nearest = r

    # add distance to total
    total += abs(nearest - head)  
    head = nearest
    seq.append(nearest)
    reqs.remove(nearest)

print("Seek sequence:", seq)
print("Total seek:", total)
