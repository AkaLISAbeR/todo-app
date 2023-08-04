"""filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for file in filenames:
    someFile = open(f"{file}", 'w')
    someFile.writelines("Hello")
    someFile.close()"""


"""def get_max():
    grades = [9.6, 9.2, 9.7]
    holder = 0
    for i in grades:
        holder = max(grades)
    return holder


print(get_max())"""


"""def get_maximum():
    celsius = [14, 15.1, 12.3]
    maximum = max(celsius)
    return maximum


celsius = get_maximum()
fahrenheit = celsius * 1.8 + 32

print(fahrenheit)
"""


"""def strength(password):
    indicator = "Strong Password"
    someList = []
    isGreaterThanEight = False
    hasOneUpper = False
    hasOneDigit = False

    if len(password) >= 8:
        isGreaterThanEight = True
    for char in password:
        if char.isupper():
            hasOneUpper = True
        if char.isdigit():
            hasOneDigit = True

    someList = [isGreaterThanEight, hasOneUpper, hasOneDigit]
    if all(someList) == False:
        indicator = "Weak Password"

    return indicator


print(strength("hotdoG"))


"""


"""def concatenator(first_string, second_string):
    pinagsama = first_string + second_string
    return pinagsama


print(concatenator("hotdog", " ni Maron"))"""


"""def speed(distance, time):
    return distance / time


print(speed(200, 4))"""


"""def speed(distance, time):
    return distance / time


print(speed(300, 5))"""


"""def get_nr_items(aList):
    items_in_list = len(aList)
    return items_in_list


global_list = ["hi", "hello","hotdog"]
print(get_nr_items(global_list))"""


def string_count(some_string):
    indicator = True
    if len(some_string) < 8:
        indicator = False
    return indicator


print(string_count("mypass"))