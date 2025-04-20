# Speed of light constant in meters per second
C = 299_792_458

def main():
    # Prompt the user for mass in kilograms
    mass = float(input("Enter kilos of mass: "))
    
    # Calculate the energy
    energy = mass * C**2

    print("\ne = m * C^2...\n")
    print(f"m = {mass} kg")
    print(f"C = {C} m/s\n")
    print(f"{energy} joules of energy!")

if __name__ == '__main__':
    main()
