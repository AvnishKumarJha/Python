
num = int(input("Enter an integer: "))


print(f"Multiplication table of {num}:")
for i in range(1, 11):
    result = num * i
    print(f"{num} x {i} = {result}")
