Absolute.value = int(input("How many sides do you want to check: "))
shapes = ["triangle","square","pentagon","hexagon","heptagon","octagon","nonagon","decagon"]
if Absolute.value > 10:
    print("Unavailable")
elif Absolute.value >= 3 and Absolute.value <= 10:
    chosen = shapes[Absolute.value - 3]
    print(chosen)

