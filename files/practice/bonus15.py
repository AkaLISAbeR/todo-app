import json

with open("questions.json", 'r') as file:  # opens the question.json file and store the values in str for to content
    content = file.read()

data = json.loads(content)  # converts the str file into a list

score = 0
for questions in data:  # iterates the contents of data to be used
    print(questions["questions"])
    for index, alt in enumerate(questions["alternatives"]):
        print(index + 1, " - ", alt)
    user_choice = int(input("Enter you number answer: "))
    questions["user_choice"] = user_choice
    if questions["correct_answer"] == questions["user_choice"]:
        score = score + 1

for index, questions in enumerate(data):
    message = f"Question: {index + 1} | Your Answer: {questions['user_choice']} | Correct Answer: {questions['correct_answer']}"
    print(message)

print("Score: ",score, " / ", len(data))



