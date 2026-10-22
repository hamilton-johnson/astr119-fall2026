# checkpoint2_practice.py -- practice problems for Checkpoint 2 (loops, lists, functions)
# Do each problem on PAPER first. Write your prediction in the comment, then run to check.

# --- Problem 1: predict the output -------------------------------------------
total = 0
for i in range(1, 6, 2):
    total = total + i
    print(i, total)
print("final:", total)
# My prediction (every line it prints):
#

# --- Problem 2: list indexing and slicing ------------------------------------
masses = [0.33, 4.87, 5.97, 0.642, 1898]   # 10^24 kg: Mercury, Venus, Earth, Mars, Jupiter
print(masses[1])
print(masses[-1])
print(masses[1:3])
print(len(masses[::2]))
# My prediction (4 lines):
#

# --- Problem 3: trace by hand ------------------------------------------------
values = [3, 8, 1, 9, 4]
biggest = values[0]
for v in values:
    if v > biggest:
        biggest = v
print("biggest:", biggest)
# Fill in the value of biggest at the END of each pass:
#   v = 3 -> biggest =
#   v = 8 -> biggest =
#   v = 1 -> biggest =
#   v = 9 -> biggest =
#   v = 4 -> biggest =

# --- Problem 4: spot the bug -------------------------------------------------
def au_to_km(d_au):
    """Convert a distance in astronomical units to kilometres."""
    km = d_au * 1.496e8
    print(km)

mars = au_to_km(1.52)
print("Mars distance:", mars)
# What does the last line actually print? Which line is the bug, and what's the fix?
#
