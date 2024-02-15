from collections import deque

jobs = deque([int(el) for el in input().split(', ')])
index_of_interest = int(input())
cycles = 0
sorted_jobs = deque(sorted(jobs))

for job in sorted_jobs:
    cycles += job
    jobs_index = jobs.index(job)
    jobs[jobs_index] = ''
    if jobs_index == index_of_interest:
        break

print(cycles)
