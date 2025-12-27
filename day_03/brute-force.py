def find_max_joltage(bank_str):
    digits = [int(x) for x in bank_str]
    max_joltage = 0
    
    # Try all pairs where i < j (maintaining order)
    for i in range(len(digits)):
        for j in range(i+1, len(digits)):
            # Form number: first digit * 10 + second digit
            joltage = digits[i] * 10 + digits[j]
            max_joltage = max(max_joltage, joltage)
    
    return max_joltage

# Apply to all banks
total = 0
with open("batteries.txt") as f:
    for line in f:
        total += find_max_joltage(line.strip())

print("Part 1 answer:", total)
