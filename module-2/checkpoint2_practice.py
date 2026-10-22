# checkpoint2_practice.py -- practice problems for Checkpoint 2 (loops, lists, functions)
# Do each problem on PAPER first. Write your prediction in the comment, then run to check.

# --- Problem 1: predict the output -------------------------------------------
total = 0
for i in range(1, 6, 2):
    total = total + i
    print(i, total)
print("final:", total)
# My prediction (every line it prints):
#1 1 /3 4 /5 9 / finals: 9

# --- Problem 2: list indexing and slicing ------------------------------------
masses = [0.33, 4.87, 5.97, 0.642, 1898]   # 10^24 kg: Mercury, Venus, Earth, Mars, Jupiter
print(masses[1])
print(masses[-1])
print(masses[1:3])
print(len(masses[::2]))
# My prediction (4 lines):
# 4.87 / 1898 / [4.87, 5.97] / 3

# --- Problem 3: trace by hand ------------------------------------------------
values = [3, 8, 1, 9, 4]
biggest = values[0]
for v in values:
    if v > biggest:
        biggest = v
print("biggest:", biggest)
# Fill in the value of biggest at the END of each pass:
#   v = 3 -> biggest = 3
#   v = 8 -> biggest = 8
#   v = 1 -> biggest = 8
#   v = 9 -> biggest = 9
#   v = 4 -> biggest = 9

# --- Problem 4: spot the bug -------------------------------------------------
def au_to_km(d_au):
    """Convert a distance in astronomical units to kilometres."""
    km = d_au * 1.496e8
    print(km)

mars = au_to_km(1.52)
print("Mars distance:", mars)
# What does the last line actually print? Which line is the bug, and what's the fix?
# last line prints mars distance: none, change print to return in the function

# --- Problem 5: write the function -------------------------------------------
def mean_temp(temps):
    """Return the average of a list of temperatures (in K).

    Use a for loop -- no sum() or numpy -- the way you would on paper.
    """
    # TODO(human):
    #   1. start a running total at 0
    #   2. loop over temps, adding each one to the total
    #   3. divide the total by how many temperatures there are
    #   4. return the result (return, not print!)
    total = 0
    for temp in temps:
        total = total + temp
    return total / len(temps)
    

planet_temps = []   # K: Mercury, Venus, Earth, Mars (mean surface)
print("mean temp:", mean_temp(planet_temps))
# My prediction (work it out by hand first):
# 418.75
