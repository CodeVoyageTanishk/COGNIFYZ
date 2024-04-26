def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
def main():
    print("Temperature Converter Program")
    while True:
        print("\n1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")
        if choice == '1':
            celsius = float(input("Enter temperature in Celsius: "))
            converted_temp = celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C is equal to {converted_temp}°F")
        elif choice == '2':
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            converted_temp = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F is equal to {converted_temp}°C")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
if __name__ == "__main__":
    main()
