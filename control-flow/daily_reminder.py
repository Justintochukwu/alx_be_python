Task = input("Enter your task: ")

Priority = input("Priority (high, medium, low): ").lower()

Time_bound = input("Is it time-bound? (yes or no): ").lower()
  
match Priority:
    case "high":
        if Time_bound == "yes":
            print(f"Reminder: '{Task}' is high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{Task}' is high priority task. Try to to complete it as soon as possible.")
    case "medium":
        if Time_bound == "yes":
            print(f"Reminder: '{Task}' is a medium priority task that should be done today.")
        else:
            print(f"Reminder: '{Task}' is a medium priority task. Schedule it for this week.")
    case "low":
        if Time_bound == "yes":
            print(f"Reminder: '{Task}' is a low priority task but still needs attention today.")
        else:
            print(f"Note: '{Task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority level entered. Please use 'high'. 'medium'. 'low'.")