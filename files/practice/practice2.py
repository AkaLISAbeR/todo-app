"""differentFiles = ["a.txt", "b.txt", "c.txt"]

for aFile in differentFiles:
    file = open(aFile, "r")
    content = file.read()
    print(content)
    file.close()"""

password = input("Enter a new password: ")

if len(password) > 7:
    print("Great password there")
elif password == 7:
    print("Password is OK, but not too strong")
else:
    print("Your password is weak")