task_variable = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: {task_variable} is a high priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"Reminder: {task_variable} is a high priority task. Consider completing it when you have free time.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: {task_variable} is a medium priority task that requires normal attention today!")
        elif time_bound == "no":
            print(f"Reminder: {task_variable} is a medium priority task. Consider completing it when you have free time.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: {task_variable} is a low priority task that requires attention")
        elif time_bound == "no":
            print(f"Note: {task_variable} is a low priority task. Consider completing it when you have free time.")
    case _:
        print("invalid priority level.")