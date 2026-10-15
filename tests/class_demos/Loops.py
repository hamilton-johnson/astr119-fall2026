# if statements
def if_statements():
    a = 3
    b = 4
    if a == b: 
        print("a is equal to b")
    else:
        print('a is not equal to b')

# if_statements()
# for loops
def for_loop(x):
    if x == "a":
        for i in range(5):
            print(i)

    if x == "b":
        for i in range(2, 6):
            print(i)

    if x == "c":
        for i in range(2,6,2):
            print(i)

    if x == "d":
        for i in range(1,4):
            for j in range(1,4):
                print(i + j, end = "")
            print("\n")

# for_loop("a")
# for_loop("b")
# for_loop("c")
# for_loop("d")

# lists

def lists(x):
    planet_1 = "WASP-39b"
    planet_2 = "51-Peg"
    planet_3 = "Jupiter"
    if x == "a":
        planets = [planet_1, planet_2, planet_3]
        print(planets)
        print(planets[0])

    if x == "a":
        for i in range(len(planets)):
            print("planet is ", planets[i])
# lists("a")
