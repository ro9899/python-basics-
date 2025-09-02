# Day 5 - Advanced Loops in Python

# Example 1: while loop
# A while loop runs until the condition becomes False
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1   # increase count by 1 each time

# Example 2: for loop with else
# The else block runs only if the loop finishes normally (no break)
for i in range(3):
    print("Iteration:", i)
else:
    print("Loop finished without break")

# Example 3: break in loop
# 'break' stops the loop immediately when condition is met
for num in range(1, 6):
    if num == 3:
        print("Breaking the loop at:", num)
        break
    print(num)

# Example 4: continue in loop
# 'continue' skips the current iteration and jumps to the next
for num in range(1, 6):
    if num == 3:
        print("Skipping number:", num)
        continue
    print(num)

# Example 5: Nested loops
# A loop inside another loop (useful for patterns, grids, etc.)
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")
