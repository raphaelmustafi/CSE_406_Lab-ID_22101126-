# priority scheduling
n = int(input("How many process: "))

pid = []
at = []
bt = []
pri = []
ct = [0]*n
tat = [0]*n
wt = [0]*n

for i in range(n):
    pid.append(input("Pid: "))
    at.append(int(input("AT: ")))
    bt.append(int(input("BT: ")))
    pri.append(int(input("Priority: ")))

done = [False]*n
time = 0

for _ in range(n):
    chosen_process = -1
    for i in range(n):
        if not done[i] and at[i] <= time:
            if chosen_process == -1 or pri[i] < pri[chosen_process]:
                chosen_process = i
    if chosen_process == -1:
        time += 1
        continue
    time += bt[chosen_process]
    ct[chosen_process] = time
    tat[chosen_process] = ct[chosen_process] - at[chosen_process]
    wt[chosen_process] = tat[chosen_process] - bt[chosen_process]
    done[chosen_process] = True

avg_wt = sum(wt) / n

print("Pid\tAT\tBT\tPri\tCT\tTAT\tWT")
for i in range(n):
    print(pid[i], "\t", at[i], "\t", bt[i], "\t", pri[i], "\t", ct[i], "\t", tat[i], "\t", wt[i])
print("Average WT:", round(avg_wt, 2))
