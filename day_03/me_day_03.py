'''
=======================================================================
ADVENT OF CODE 2025 - Day 3: Lobby
=======================================================================
'''
import time

#Timing: Star
start = time.perf_counter()

total_joltage = 0

with open(r"batteries.txt") as f:

    for line in f:

        line = line.strip()
        d_max = max(line)
        

        if line.count(d_max) > 1:
            total_joltage += int(d_max * 2)            
        else:
            idx = line.find(d_max)

            if idx == len(line) - 1:
                d_second = max(line[:-1])
                total_joltage += int(d_second + d_max)
            else:
                d_second = max(line[idx+1:])
                total_joltage += int(d_max + d_second)

                
print(f"Part 1 answer : {total_joltage}")


# Greedy Left-to-Right Algorithm

def find_largest_n_digit_number(s, n):
    result = []
    start_pos = 0
    
    for _ in range(n):
        can_skip = len(s) - start_pos - (n - len(result))
        search_segment = s[start_pos : start_pos + can_skip + 1]
        max_digit = max(search_segment)
        best_pos = start_pos + search_segment.index(max_digit)
        
        result.append(max_digit)
        start_pos = best_pos + 1
    
    return ''.join(result)


total_sum = []

with open(r"batteries.txt") as f:

    for line in f:        
        total_sum.append(int(find_largest_n_digit_number(line.strip(), 12)))

print("Part 2 answer : ", sum(total_sum))


#Timing: End
end = time.perf_counter()
print(f"\nTime to complete = {(end-start)*1000:.2f} milliseconds.")


