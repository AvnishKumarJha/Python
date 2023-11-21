list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]


if len(list1) != len(list2):
    print("Lists must have the same length for index-wise addition.")
else:
    result = []

    for i in range(len(list1)):
        result.append(list1[i] + list2[i])

    print(result)
