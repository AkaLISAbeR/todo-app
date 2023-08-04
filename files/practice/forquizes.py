def identifyTemp(temp):
    low_limit = 15
    high_limit = 25
    if temp > high_limit:
        print("Hot")
    elif temp >= 15 and temp <= high_limit:
        print("Warm")
    else:
        print("Cold")

identifyTemp(26)