n = 4

for i in range(n):

    for k in range(i + 1):
        print("*", end="")

    for j in range(n - i - 1):
        print(" ", end="")

    for l in range(n, i + 1, -1):
        print(" ", end="")

    for m in range(i + 1):
        print("*", end="")

    print()
