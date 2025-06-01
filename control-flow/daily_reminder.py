task = input("Enter your task: ")

priority = input("Priority (high, medium, low): ").lower()

time_bound = input("Is it time-bound? (yes or no): ").lower()
  
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task that requires immediate attention today!"
    case "medium":
        reminder = f"Reminder: '{task}' is a high priority task that requires immediate attention today!"
    case "low":
        reminder = f"Reminder: '{task}' is a high priority task that requires immediate attention today!"
    case _:
        reminder = f"Reminder: '{task}' is a high priority task that requires immediate attention today!"
              
if time_bound == "yes":
    reminder += "{reminder}"
  
print(reminder)