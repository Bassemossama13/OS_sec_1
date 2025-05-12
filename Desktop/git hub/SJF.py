# Process structure: [Process ID, Arrival Time, Burst Time]
processes = [
    ["P1", 0, 7],
    ["P2", 2, 4],
    ["P3", 4, 1],
    ["P4", 5, 4],
]

# Sort by arrival time initially
processes.sort(key=lambda x: x[1])

time = 0
completed = []
waiting_times = {}
turnaround_times = {}

while processes:
    # Get available processes that have arrived
    available = []
    for p in processes:
        if p[1] <= time:
            available.append(p)

    
    if not available:
        # No process available yet, advance time
        time += 1
        continue

    # Select process with shortest burst time
    next_proc = min(available, key=lambda x: x[2])
    processes.remove(next_proc)

    pid = next_proc[0]      # Process ID (e.g., "P2")
    arrival = next_proc[1]  # Arrival time (e.g., 2)
    burst = next_proc[2]    # Burst time (e.g., 4)


    # Calculate waiting time
    wait = time - arrival
    waiting_times[pid] = wait

    # Calculate turnaround time
    tat = wait + burst
    turnaround_times[pid] = tat

    # Move time forward
    time += burst
    completed.append(pid)

# Print results
print("Process | Waiting Time | Turnaround Time")
for pid in completed:
    print(pid, "|", waiting_times[pid], "|", turnaround_times[pid])


# Average times
avg_wait = sum(waiting_times.values()) / len(waiting_times)
avg_tat = sum(turnaround_times.values()) / len(turnaround_times)

print(f"\nAverage Waiting Time: {avg_wait:.2f}")
print(f"Average Turnaround Time: {avg_tat:.2f}")
