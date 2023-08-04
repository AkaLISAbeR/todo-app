password = input("Enter a Password: ")
result = {}

if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

isANumber = False
for i in password:
    if i.isdigit():
        isANumber = True

result["isANumber"] = isANumber

hasUpper = False
for i in password:
    if i.isupper():
        hasUpper = True

result["hasUpper"] = hasUpper

print(result)
if all(result):
    print("Strong Password")
else:
    print("Weak Password")