FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def main():
    try:
        temp_input = input("Enter the temperature (eg.,100): ").strip()
        temp = float(temp_input)
    except ValueError:
        raise ValueError("Invalid tempereature. Please enter a numeric value.")
    
    unit = input("Is the temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    
    if unit == 'F':
        converted = convert_to_celsius(temp)
        print(f"{temp}°F is {converted:.2F}°C")
    
    elif unit == 'C':
        converted = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {converted:.2F}°F")
    else:
        raise ValueError("Invalid temperature unit. Please enter 'C' or 'F'.")
    
if __name__=="__main__":
    main()