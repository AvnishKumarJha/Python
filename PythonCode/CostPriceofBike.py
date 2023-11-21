cost_price = float(input("Enter the cost price of the bike (in Rs): "))


if cost_price > 100000:
    road_tax = cost_price * 0.15
elif cost_price > 50000:
    road_tax = cost_price * 0.10
else:
    road_tax = cost_price * 0.05


print("Road tax to be paid: Rs", road_tax)
