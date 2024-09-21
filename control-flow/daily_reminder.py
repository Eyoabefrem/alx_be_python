Task = input("Enter the task description:")
Priority = input("Enter the task's priority (high, medium, low):").lower()
Time_Bound = input("Is the task time-bound? (yes or no): ").lower()
match Priority:
    case "high":
        reminder = f"Task: {Task} has a high priority"
    case "medium":
        reminder = f"Task: {Task} has a medium priority"
    case "low":
        reminder = f"Task: {Task} has a low priority"
    case _:
        reminder = f"Task: {Task} has an unknown priority level"
if Time_Bound == "yes":
    reminder += " and requires immediate attention today!"
else:
    reminder += " but is not time-bound."
print(reminder)