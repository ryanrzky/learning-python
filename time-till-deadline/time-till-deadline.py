from datetime import datetime

userInput = input("Enter your goal with a deadline seperated by colon\n")
inputList = userInput.split(":")

goal = inputList[0]
deadline = inputList[1]

deadlineDate = datetime.strptime(deadline, "%d.%m.%Y")
todayDate = datetime.today()

timeTill = deadlineDate - todayDate
hoursTill = int(timeTill.total_seconds() / 60 / 60) # artinya detik di bagi 60 60

print(f"Dear user, time remmaining for your goal: {goal} is {timeTill} days")