task = input("Enter your task: ")

priority = input("Priority (high, medium, low): ").lower()

time_bound = input("Is it time-bound? (yes or no): ").lower()
  
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task that requires immediate attention today!"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium"
    case "low":
        reminder = f"Reminder: '{task}' is a low priority task. Consider completing it when you have free time."
              
if time_bound == "yes":
    reminder += "{reminder}"
  
print(reminder)