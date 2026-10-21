n = int(input("n: "))
for i in range(1, n + 1):
    for k in range(1, n + 1):
        print(i * k, end = " ")
    print("\n")