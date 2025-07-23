n = int(input("How many processes? "))

pid = []
at = []
bt = []

for i in range(n):
    print("Process", i+1)
    pid.append(input("Process ID: "))
    at.append(int(input("Arrival Time: ")))
    bt.append(int(input("Burst Time: ")))

ct = [0]*n
tat = [0]*n
wt = [0]*n
done = [0]*n

time = 0
finished = 0

#Loop until all processes are finished

while finished < n:
    small = -1
    for i in range(n):
        if at[i] <= time and done[i] == 0:
            if small == -1 or bt[i] < bt[small]:
                small = i

    if small == -1:
        time += 1
    else:
        time = time + bt[small]
        ct[small] = time
        tat[small] = ct[small] - at[small]
        wt[small] = tat[small] - bt[small]
        done[small] = 1
        finished += 1

print("\nPID\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    print(pid[i], "\t", at[i], "\t", bt[i], "\t", ct[i], "\t", tat[i], "\t", wt[i])

print("\nAvg TAT:", round(sum(tat)/n, 2))
print("Avg WT :", round(sum(wt)/n, 2))
