def print_alternate_square_and_cube(start, end):
    for num in range(start, end + 1):
        if num % 2 == 0:
            print(num, num ** 3, "--> Cube")
        else:
            print(num, num ** 2, "--> Square")


start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))


print_alternate_square_and_cube(start_range, end_range)
