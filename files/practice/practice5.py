"""try:
    width = float(input("Please enter a width: "))
    height = float(input("Please enter a height: "))

    if width == height:
        exit("The object is a square")

    area = width * height
    print(area)
except ValueError:
    print("Please enter a number")

try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))

    percentage = value / total_value * 100
    print(f"That is {percentage}")

except ValueError:
    print("Please enter a number")"""

try:
    waiting_list = ["john", "marry"]
    name = input("Enter name: ")

    number = waiting_list.index(name)
    print(f"{name}'s turn is {number}")
except ValueError:
    print("The name is not in the list")