def main():
    # Prompt the user for a temperature in Fahrenheit
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))

    # Convert the temperature to Celsius
    celsius = (fahrenheit - 32) * 5.0 / 9.0

    print(f"Temperature: {fahrenheit}F = {celsius}C")

if __name__ == '__main__':
    main()
