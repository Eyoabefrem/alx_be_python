task = input("Enter the task description:")
priority = input("Enter the task's priority (high, medium, low):").lower()
time_bound = input("Is the task time-bound? (yes or no): ").lower()
match priority:
    case "high":
        reminder = f"Task: {task} has a high priority"
    case "medium":
        reminder = f"Task: {task} has a medium priority"
    case "low":
        reminder = f"Task: {task} has a low priority"
    case _:
        reminder = f"Task: {task} has an unknown priority level"
if time_bound == "yes":
    reminder += " and requires immediate attention today!"
else:
    reminder += " but is not time-bound."
print(reminder)