n = int(input("Enter number of processes: "))

pid = []
at = []
bt = []

for i in range(n):
    print("Process", i + 1)
    pid.append(input("Process ID: "))
    at.append(int(input("Arrival Time: ")))
    bt.append(int(input("Burst Time: ")))

# Bubble sort based on arrival time
for i in range(n - 1):
    for j in range(i + 1, n):
        if at[i] > at[j]:
            at[i], at[j] = at[j], at[i]
            bt[i], bt[j] = bt[j], bt[i]
            pid[i], pid[j] = pid[j], pid[i]

ct = [0] * n
tat = [0] * n
wt = [0] * n

# First process completion time
ct[0] = at[0] + bt[0]
tat[0] = ct[0] - at[0]
wt[0] = tat[0] - bt[0]

# Calculate for rest of the processes
for i in range(1, n):
    if ct[i-1] < at[i]:
        ct[i] = at[i] + bt[i]
    else:
        ct[i] = ct[i-1] + bt[i]

    tat[i] = ct[i] - at[i]
    wt[i] = tat[i] - bt[i]

print("\nPID\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    print(pid[i], "\t", at[i], "\t", bt[i], "\t", ct[i], "\t", tat[i], "\t", wt[i])

print("\nAverage Turnaround Time:", round(sum(tat) / n, 2))
print("Average Waiting Time   :", round(sum(wt) / n, 2))
