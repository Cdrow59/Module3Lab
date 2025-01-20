# Author: Clayton Drown
# File Name: Module3Lab.py
# Description: This program ask users info about a car, stores it in classes and displays it in a easy to read format.


class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type  # Initialize the vehicle type


class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)  # Call the parent class (Vehicle) constructor
        self.year = year  # Initialize the year of the automobile
        self.make = make  # Initialize the make of the automobile
        self.model = model  # Initialize the model of the automobile
        self.doors = doors  # Initialize the number of doors of the automobile
        self.roof = roof  # Initialize the type of roof of the automobile


def main():
    vehicle_type = "car"  # Set the vehicle type to car
    year = input("Enter the year of the car: ")  # Get the year from the user
    make = input("Enter the make of the car: ")  # Get the make from the user
    model = input("Enter the model of the car: ")  # Get the model from the user
    doors = input("Enter the number of doors (2 or 4): ")  # Get the number of doors from the user
    roof = input("Enter the type of roof (solid or sun roof): ")  # Get the type of roof from the user

    car = Automobile(vehicle_type, year, make, model, doors, roof)  # Create an instance of Automobile

    # Print the vehicle information
    print("\nVehicle Information:")
    print(f"  Vehicle type: {car.vehicle_type}")
    print(f"  Year: {car.year}")
    print(f"  Make: {car.make}")
    print(f"  Model: {car.model}")
    print(f"  Number of doors: {car.doors}")
    print(f"  Type of roof: {car.roof}")


if __name__ == "__main__":
    main()  # Call the main function if the script is executed directly
