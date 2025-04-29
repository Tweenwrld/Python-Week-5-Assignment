class Vehicle:
    """Base class for all vehicles."""
    
    def __init__(self, make, model, year, color):
        """Initialize a vehicle with basic attributes.
        
        Args:
            make (str): The manufacturer of the vehicle
            model (str): The model name of the vehicle
            year (int): The year the vehicle was manufactured
            color (str): The color of the vehicle
        """
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0
        self.is_running = False
        
    def start(self):
        """Start the vehicle's engine."""
        if not self.is_running:
            self.is_running = True
            print(f"The {self.color} {self.year} {self.make} {self.model} has started.")
        else:
            print(f"The {self.make} {self.model} is already running.")
    
    def stop(self):
        """Stop the vehicle's engine."""
        if self.is_running:
            self.is_running = False
            self.speed = 0
            print(f"The {self.make} {self.model} has stopped.")
        else:
            print(f"The {self.make} {self.model} is already off.")
    
    def move(self):
        """Base method for movement - to be overridden by subclasses."""
        if self.is_running:
            print(f"The {self.make} {self.model} is moving.")
        else:
            print(f"You need to start the {self.make} {self.model} first.")
    
    def accelerate(self, speed_increase):
        """Increase the speed of the vehicle.
        
        Args:
            speed_increase (int): The amount to increase speed by
        """
        if self.is_running:
            self.speed += speed_increase
            print(f"The {self.make} {self.model} accelerates to {self.speed} km/h.")
        else:
            print(f"You need to start the {self.make} {self.model} first.")
    
    def brake(self, speed_decrease):
        """Decrease the speed of the vehicle.
        
        Args:
            speed_decrease (int): The amount to decrease speed by
        """
        if self.is_running:
            if speed_decrease > self.speed:
                self.speed = 0
            else:
                self.speed -= speed_decrease
            print(f"The {self.make} {self.model} slows down to {self.speed} km/h.")
        else:
            print(f"The {self.make} {self.model} is not running.")
    
    def __str__(self):
        """String representation of the vehicle."""
        status = "running" if self.is_running else "off"
        return f"{self.year} {self.make} {self.model} ({self.color}) - {status}, {self.speed} km/h"


class Car(Vehicle):
    """Class representing cars, inheriting from Vehicle."""
    
    def __init__(self, make, model, year, color, fuel_type, doors):
        """Initialize a car with car-specific attributes.
        
        Args:
            make (str): The manufacturer of the car
            model (str): The model name of the car
            year (int): The year the car was manufactured
            color (str): The color of the car
            fuel_type (str): The type of fuel the car uses
            doors (int): The number of doors the car has
        """
        super().__init__(make, model, year, color)
        self.fuel_type = fuel_type
        self.doors = doors
        self.is_convertible = False
        
    def move(self):
        """Override the move method for cars."""
        if self.is_running:
            print(f"The {self.color} {self.make} {self.model} is driving on the road. 🚗")
        else:
            print(f"You need to start the {self.make} {self.model} first.")
    
    def honk(self):
        """Cars can honk their horn."""
        print(f"The {self.make} {self.model} honks: BEEP BEEP!")
    
    def park(self):
        """Park the car."""
        if self.speed == 0:
            print(f"The {self.make} {self.model} is now parked.")
        else:
            print(f"You need to stop the {self.make} {self.model} before parking.")


class Motorcycle(Vehicle):
    """Class representing motorcycles, inheriting from Vehicle."""
    
    def __init__(self, make, model, year, color, engine_size, has_sidecar):
        """Initialize a motorcycle with motorcycle-specific attributes.
        
        Args:
            make (str): The manufacturer of the motorcycle
            model (str): The model name of the motorcycle
            year (int): The year the motorcycle was manufactured
            color (str): The color of the motorcycle
            engine_size (int): The engine size in cc
            has_sidecar (bool): Whether the motorcycle has a sidecar
        """
        super().__init__(make, model, year, color)
        self.engine_size = engine_size
        self.has_sidecar = has_sidecar
        
    def move(self):
        """Override the move method for motorcycles."""
        if self.is_running:
            print(f"The {self.engine_size}cc {self.make} {self.model} is zooming through traffic. 🏍️")
        else:
            print(f"You need to start the {self.make} {self.model} first.")
    
    def pop_wheelie(self):
        """Motorcycles can pop a wheelie."""
        if self.is_running and self.speed > 20:
            print(f"The {self.make} {self.model} pops an impressive wheelie!")
        else:
            print(f"The {self.make} {self.model} needs to be going faster to pop a wheelie.")
    
    def rev_engine(self):
        """Motorcycles can rev their engine."""
        if self.is_running:
            print(f"The {self.make} {self.model} revs loudly: VROOM VROOM!")
        else:
            print(f"You need to start the {self.make} {self.model} first.")


class Boat(Vehicle):
    """Class representing boats, inheriting from Vehicle."""
    
    def __init__(self, make, model, year, color, boat_type, length):
        """Initialize a boat with boat-specific attributes.
        
        Args:
            make (str): The manufacturer of the boat
            model (str): The model name of the boat
            year (int): The year the boat was manufactured
            color (str): The color of the boat
            boat_type (str): The type of boat (e.g., sailboat, motorboat)
            length (float): The length of the boat in meters
        """
        super().__init__(make, model, year, color)
        self.boat_type = boat_type
        self.length = length
        self.is_anchored = False
        
    def move(self):
        """Override the move method for boats."""
        if self.is_running and not self.is_anchored:
            print(f"The {self.length}m {self.boat_type} {self.make} {self.model} is sailing across the water. ⛵")
        elif self.is_anchored:
            print(f"The {self.make} {self.model} is anchored and cannot move.")
        else:
            print(f"You need to start the {self.make} {self.model} first.")
    
    def anchor(self):
        """Drop the boat's anchor."""
        if not self.is_anchored:
            self.is_anchored = True
            self.speed = 0
            print(f"The {self.make} {self.model} has dropped its anchor.")
        else:
            print(f"The {self.make} {self.model} is already anchored.")
    
    def raise_anchor(self):
        """Raise the boat's anchor."""
        if self.is_anchored:
            self.is_anchored = False
            print(f"The {self.make} {self.model} has raised its anchor.")
        else:
            print(f"The {self.make} {self.model} is not anchored.")


class Plane(Vehicle):
    """Class representing planes, inheriting from Vehicle."""
    
    def __init__(self, make, model, year, color, max_altitude, num_engines):
        """Initialize a plane with plane-specific attributes.
        
        Args:
            make (str): The manufacturer of the plane
            model (str): The model name of the plane
            year (int): The year the plane was manufactured
            color (str): The color of the plane
            max_altitude (int): The maximum altitude in feet
            num_engines (int): The number of engines
        """
        super().__init__(make, model, year, color)
        self.max_altitude = max_altitude
        self.num_engines = num_engines
        self.altitude = 0
        self.is_landed = True
        
    def move(self):
        """Override the move method for planes."""
        if self.is_running and not self.is_landed:
            print(f"The {self.make} {self.model} with {self.num_engines} engines is flying through the sky at {self.altitude} feet. ✈️")
        elif self.is_landed:
            print(f"The {self.make} {self.model} needs to take off first.")
        else:
            print(f"You need to start the {self.make} {self.model} first.")
    
    def take_off(self):
        """Take off the plane."""
        if self.is_running and self.is_landed and self.speed >= 120:
            self.is_landed = False
            self.altitude = 1000
            print(f"The {self.make} {self.model} takes off and climbs to {self.altitude} feet!")
        elif not self.is_running:
            print(f"You need to start the {self.make} {self.model} first.")
        elif not self.is_landed:
            print(f"The {self.make} {self.model} is already in the air.")
        else:
            print(f"The {self.make} {self.model} needs to reach at least 120 km/h to take off.")
    
    def land(self):
        """Land the plane."""
        if self.is_running and not self.is_landed:
            self.is_landed = True
            self.altitude = 0
            self.speed = 0
            print(f"The {self.make} {self.model} has safely landed.")
        elif self.is_landed:
            print(f"The {self.make} {self.model} is already on the ground.")
        else:
            print(f"You need to start the {self.make} {self.model} first.")
    
    def change_altitude(self, altitude_change):
        """Change the altitude of the plane.
        
        Args:
            altitude_change (int): The amount to change altitude by (can be positive or negative)
        """
        if self.is_running and not self.is_landed:
            new_altitude = self.altitude + altitude_change
            if new_altitude <= 0:
                print(f"Cannot descend below 0 feet. Please land the plane.")
            elif new_altitude > self.max_altitude:
                print(f"Cannot exceed maximum altitude of {self.max_altitude} feet.")
            else:
                self.altitude = new_altitude
                direction = "climbs" if altitude_change > 0 else "descends"
                print(f"The {self.make} {self.model} {direction} to {self.altitude} feet.")
        elif self.is_landed:
            print(f"The {self.make} {self.model} needs to take off first.")
        else:
            print(f"You need to start the {self.make} {self.model} first.")


# Example usage
if __name__ == "__main__":
    # Create instances of different vehicles
    tesla = Car("Tesla", "Model S", 2023, "red", "electric", 4)
    harley = Motorcycle("Harley-Davidson", "Street Glide", 2022, "black", 1868, False)
    sunseeker = Boat("Sunseeker", "Predator", 2021, "white", "yacht", 24.5)
    boeing = Plane("Boeing", "747", 2020, "blue and white", 45000, 4)
    
    # Demonstrate starting vehicles
    print("=== Starting Vehicles ===")
    tesla.start()
    harley.start()
    sunseeker.start()
    boeing.start()
    
    # Demonstrate polymorphism with the move method
    print("\n=== Movement Examples (Polymorphism) ===")
    tesla.move()       # Car's implementation
    harley.move()      # Motorcycle's implementation
    sunseeker.move()   # Boat's implementation
    boeing.move()      # Plane's implementation
    
    # Demonstrate vehicle-specific methods
    print("\n=== Vehicle-Specific Methods ===")
    tesla.accelerate(60)
    tesla.honk()
    
    harley.accelerate(80)
    harley.pop_wheelie()
    
    sunseeker.accelerate(30)
    sunseeker.anchor()
    sunseeker.move()  # Should show that it's anchored
    
    boeing.accelerate(200)
    boeing.take_off()
    boeing.move()  # Should show flying
    boeing.change_altitude(10000)
    
    # Stop all vehicles
    print("\n=== Stopping Vehicles ===")
    tesla.stop()
    harley.stop()
    
    # Land the plane before stopping
    boeing.land()
    boeing.stop()
    
    # Try to move again after stopping
    print("\n=== Trying to Move After Stopping ===")
    tesla.move()  # Should show that it needs to be started first