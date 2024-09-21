Task = input("Enter your task:")
Priority = input("Priority (high/medium/low):").lower()
Time_Bound = input("Is it time-bound? (yes/no):").lower()
match Priority:
    case "high":
        reminder = f"Task: {Task} is a high priority"
    case "medium":
        reminder = f"Task: {Task} is a medium priority"
    case "low":
        reminder = f"Task: {Task} is a low priority"
    case _:
        reminder = f"Task: {Task} is an unknown priority level"
if Time_Bound == "yes":
    reminder += " that requires immediate attention today!!"
else:
    reminder += " but is not time-bound."
print(reminder)