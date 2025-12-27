'''
=======================================================================
ADVENT OF CODE 2025 - Day 2: Gift Shop
=======================================================================
'''
import time

#Timing: Star
start = time.perf_counter()
wrong_ids = []

with open(r"ids.txt") as f:
    ranges = f.read().split(',')
    
    
for r in ranges:
    low, high = r.split('-')
    for number in range(int(low), int(high) + 1):
        number_str = str(number)
        length = len(number_str)
        if length % 2 == 0:
            half = length // 2
            if number_str[:half] == number_str[half:]:
                wrong_ids.append(number)

print("Part 1 answer : ", sum(wrong_ids))

wrong_ids_part2 = []

for r in ranges:
    low, high = r.split('-')
    for number in range(int(low), int(high) + 1):
        number_str = str(number)
        length = len(number_str)
        for sub_len in range(1, length // 2 + 1):
            if length % sub_len == 0:
                repeats = length // sub_len
                substring = number_str[:sub_len]
                if substring * repeats == number_str and repeats >= 2:
                    wrong_ids_part2.append(number)
                    break  # Only count each number once

print("Part 2 answer : ", sum(wrong_ids_part2))


#Timing: End
end = time.perf_counter()
print(f"\nTime to complete = {(end-start)*1000:.2f} milliseconds.")



