from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Crrent date and time:", formatted_date)
    
def calculate_future_date(days_to_add):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)
    
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Date after {days_to_add} days will be:", formatted_future_date)
    
def main():
    display_current_datetime()
    while True:
        try:
            days_input = input("Enter the number of days to add to the current date: ")
            days = int(days_input)
            break
        except ValueError:
            print("Invalid input. Please enter an integer number of days.")
            
    calculate_future_date(days)
    
if __name__=="__main__":
    main()