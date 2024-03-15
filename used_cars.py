from car import Car

def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180, "My Car")
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)

    limo = Car(100, "Limo")
    limo.add_fuel(20)
    print(f"Amount of fuel in limo: {limo.fuel}")
    limo.drive(115)
    print(f"Current odometer reading for limo: {limo._odometer}")
    print(limo)

if __name__ == "__main__":
    main()
