age = int(input("Enter your age: "))
sex = input("Enter your sex (M/F): ")
number_of_days = int(input("Enter the number of days worked: "))


if age >= 18 and age < 30:
    if sex == 'M':
        wage_per_day = 700
    elif sex == 'F':
        wage_per_day = 750
    else:
        print("Enter appropriate sex")
        exit()
elif age >= 30 and age <= 40:
    if sex == 'M':
        wage_per_day = 800
    elif sex == 'F':
        wage_per_day = 850
    else:
        print("Enter appropriate sex")
        exit()
else:
    print("Enter appropriate age")
    exit()


total_wages = wage_per_day * number_of_days


print("Total wages: Rs", total_wages)
