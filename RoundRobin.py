n = int(input("Enter number of processes: "))
quantum = int(input("Enter time quantum: "))

process = []
at = []
bt = []

for i in range(n):
    pid = input("Enter process name: ")
    a = int(input("Enter arrival time: "))
    b = int(input("Enter burst time: "))
    process.append(pid)
    at.append(a)
    bt.append(b)

rt = bt[:]
ct = [0]*n
tat = [0]*n
wt = [0]*n
time = 0
done = 0
queue = []
visited = [0]*n

while done < n:
    for i in range(n):
        if at[i] <= time and rt[i] > 0 and visited[i] == 0:
            queue.append(i)
            visited[i] = 1

    if queue:
        p = queue.pop(0)
        if rt[p] > quantum:
            time += quantum
            rt[p] -= quantum
        else:
            time += rt[p]
            rt[p] = 0
            ct[p] = time
            done += 1

        # check for new process during execution
        for i in range(n):
            if at[i] <= time and rt[i] > 0 and visited[i] == 0:
                queue.append(i)
                visited[i] = 1

        if rt[p] > 0:
            queue.append(p)
    else:
        time += 1  # idle time

for i in range(n):
    tat[i] = ct[i] - at[i]
    wt[i] = tat[i] - bt[i]

print("\nProcess\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    print(process[i], "\t", at[i], "\t", bt[i], "\t", ct[i], "\t", tat[i], "\t", wt[i])
