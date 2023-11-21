my_list = [11, 88, 66, 44, 77, 99, 33, 1]
print("Reversed list (without a function):", my_list[::-1])


def reverse_list(input_list):
    return input_list[::-1]


reversed_list = reverse_list(my_list)
print("Reversed list (with a function):", reversed_list)
