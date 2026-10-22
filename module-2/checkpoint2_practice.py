# checkpoint2_practice.py -- practice problems for Checkpoint 2 (loops, lists, functions)
# Do each problem on PAPER first. Write your prediction in the comment, then run to check.

# --- Problem 1: predict the output -------------------------------------------
total = 0
for i in range(1, 6, 2):
    total = total + i
    print(i, total)
print("final:", total)
# My prediction (every line it prints):
#1 / 4 / 9 / finals: 9

# --- Problem 2: list indexing and slicing ------------------------------------
masses = [0.33, 4.87, 5.97, 0.642, 1898]   # 10^24 kg: Mercury, Venus, Earth, Mars, Jupiter
print(masses[1])
print(masses[-1])
print(masses[1:3])
print(len(masses[::2]))
# My prediction (4 lines):
# 4.87 / 1898 / 4.87, 5.97 / 3
