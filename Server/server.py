n, T = [int(data) for data in input().strip('\n').split()]
tasks = [int(task) for task in input().strip('\n').split()]

totalTime = 0
tasksCompleted = 0

for task in tasks:
    totalTime += task
    # take into account if final task run
    # brings totalTime == T
    if totalTime <= T:
        tasksCompleted += 1
    if T <= totalTime:
        break

print(taskscompleted)
