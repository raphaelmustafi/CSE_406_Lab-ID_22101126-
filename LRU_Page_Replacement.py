pages = list(map(int, input("Enter pages: ").split()))
n = int(input("Enter frame size: "))
frames = []
faults = 0

for p in pages:
    if p not in frames:
        if len(frames) < n:
            frames.append(p)
        else:
            frames.pop(0)
            frames.append(p)
        faults += 1
    else:
        frames.remove(p)
        frames.append(p)

print("Page Faults:", faults)

