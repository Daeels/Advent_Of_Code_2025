'''
=======================================================================
ADVENT OF CODE 2025 - Day 1: Secret Entrance
=======================================================================
'''
import time

begin = 50
begin2 = 50
rots = []
c1 = 0
c2 = 0

#Timing: Star
start = time.perf_counter()

with open(r"rotations.txt") as f:
    rots = [-int(line[1:]) if line[0] == 'L' else int(line[1:]) for line in f.read().splitlines()]


for r in rots:
    intermid = begin + r
    begin = (intermid) % 100
    if begin == 0:
        c1 += 1

print("Part 1 answer : ", c1)

# Brute force for part 2
for r in rots:
    for _ in range(abs(r)):
        begin2 += 1 if r > 0 else -1
        begin2 = begin2 % 100
        if begin2 == 0:
            c2 += 1

print("Part 2 answer : ", c2)


#Timing: End
end = time.perf_counter()
print(f"\nTime to complete = {(end-start)*1000:.2f} milliseconds.")