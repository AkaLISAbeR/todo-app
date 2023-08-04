date = input("Enter today's date: ")
mood = input("How do you rate your mood today from 1 to 10: ")
journal = input("Let your thoughts flow: ")

with open(f"Journal/{date}" , 'w') as file:
    file.writelines(mood + 2 * "\n")
    file.writelines(journal)

