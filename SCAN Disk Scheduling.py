# SCAN Disk Scheduling (direction = left)


reqs = [int(x) for x in input("Enter requests: ").split()]
head = int(input("Enter initial head position: "))

total_seek = 0
seq = []

#if there are any unsorted data incase
reqs.sort()  

# starting from left beacuse my direction is left.
left = [r for r in reqs if r <= head] 
right = [r for r in reqs if r > head]   


for r in reversed(left):
    total_seek += abs(head - r)
    head = r
    seq.append(r)


for r in right:
    total_seek += abs(head - r)
    head = r
    seq.append(r)

print("Seek sequence:", seq)
print("Total seek:", total_seek)
