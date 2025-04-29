class Animal:
    """Base class for all animals in our kingdom."""
    
    def __init__(self, name, age, weight_kg):
        """Initialize an animal with basic attributes.
        
        Args:
            name (str): The animal's name
            age (int): The animal's age in years
            weight_kg (float): The animal's weight in kilograms
        """
        self.name = name
        self.age = age
        self.weight_kg = weight_kg
        self.is_alive = True
        
    def eat(self, food):
        """Animal consumes food.
        
        Args:
            food (str): The type of food being eaten
        """
        print(f"{self.name} is eating {food}.")
        
    def sleep(self, hours):
        """Animal sleeps for the specified hours.
        
        Args:
            hours (int): Number of hours to sleep
        """
        print(f"{self.name} is sleeping for {hours} hours.")
        
    def make_sound(self):
        """Base method for making sound - to be overridden by subclasses."""
        print("Some generic animal sound")
        
    def move(self):
        """Base method for movement - to be overridden by subclasses."""
        print(f"{self.name} is moving.")
        
    def __str__(self):
        """String representation of the animal."""
        return f"{self.name}, {self.age} years old, {self.weight_kg}kg"


class Mammal(Animal):
    """Class representing mammals, inheriting from Animal."""
    
    def __init__(self, name, age, weight_kg, fur_color, is_carnivore):
        """Initialize a mammal with mammal-specific attributes.
        
        Args:
            name (str): The mammal's name
            age (int): The mammal's age in years
            weight_kg (float): The mammal's weight in kilograms
            fur_color (str): The color of the mammal's fur
            is_carnivore (bool): Whether the mammal is a carnivore
        """
        # Call the parent class constructor
        super().__init__(name, age, weight_kg)
        self.fur_color = fur_color
        self.is_carnivore = is_carnivore
        self.body_temperature = 37.0  # Celsius, typical for mammals
        
    def give_birth(self):
        """Mammal reproduction method."""
        print(f"{self.name} is giving birth to live young.")
        
    def regulate_temperature(self):
        """Mammals regulate their body temperature."""
        print(f"{self.name} is maintaining a body temperature of {self.body_temperature}°C.")


class Bird(Animal):
    """Class representing birds, inheriting from Animal."""
    
    def __init__(self, name, age, weight_kg, wingspan, can_fly):
        """Initialize a bird with bird-specific attributes.
        
        Args:
            name (str): The bird's name
            age (int): The bird's age in years
            weight_kg (float): The bird's weight in kilograms
            wingspan (float): The bird's wingspan in meters
            can_fly (bool): Whether the bird can fly
        """
        super().__init__(name, age, weight_kg)
        self.wingspan = wingspan
        self.can_fly = can_fly
        self.has_feathers = True
        
    def lay_eggs(self, number):
        """Birds lay eggs for reproduction.
        
        Args:
            number (int): Number of eggs laid
        """
        print(f"{self.name} has laid {number} eggs.")
        
    def move(self):
        """Override the move method for birds."""
        if self.can_fly:
            print(f"{self.name} is flying through the air.")
        else:
            print(f"{self.name} is walking, as it cannot fly.")
            
    def make_sound(self):
        """Override the make_sound method for birds."""
        print(f"{self.name} is chirping.")


class Reptile(Animal):
    """Class representing reptiles, inheriting from Animal."""
    
    def __init__(self, name, age, weight_kg, scale_type, is_venomous):
        """Initialize a reptile with reptile-specific attributes.
        
        Args:
            name (str): The reptile's name
            age (int): The reptile's age in years
            weight_kg (float): The reptile's weight in kilograms
            scale_type (str): The type of scales the reptile has
            is_venomous (bool): Whether the reptile is venomous
        """
        super().__init__(name, age, weight_kg)
        self.scale_type = scale_type
        self.is_venomous = is_venomous
        self.cold_blooded = True
        
    def bask(self):
        """Reptiles bask in the sun to regulate temperature."""
        print(f"{self.name} is basking in the sun to warm up.")
        
    def move(self):
        """Override the move method for reptiles."""
        print(f"{self.name} is slithering across the ground.")
        
    def make_sound(self):
        """Override the make_sound method for reptiles."""
        print(f"{self.name} is hissing.")
        
    def shed_skin(self):
        """Reptiles shed their skin."""
        print(f"{self.name} is shedding its {self.scale_type} scales.")


class Lion(Mammal):
    """Class representing lions, inheriting from Mammal."""
    
    def __init__(self, name, age, weight_kg, fur_color, mane_size=None):
        """Initialize a lion with lion-specific attributes.
        
        Args:
            name (str): The lion's name
            age (int): The lion's age in years
            weight_kg (float): The lion's weight in kilograms
            fur_color (str): The color of the lion's fur
            mane_size (str, optional): Size of the lion's mane (if male)
        """
        super().__init__(name, age, weight_kg, fur_color, True)  # Lions are carnivores
        self.mane_size = mane_size
        self.species = "Panthera leo"
        
    def make_sound(self):
        """Override the make_sound method for lions."""
        print(f"{self.name} is ROARING loudly!")
        
    def move(self):
        """Override the move method for lions."""
        print(f"{self.name} is prowling through the savanna.")
        
    def hunt(self, prey):
        """Lions hunt other animals.
        
        Args:
            prey (str): The type of animal being hunted
        """
        print(f"{self.name} is hunting {prey} with its pride.")


class Eagle(Bird):
    """Class representing eagles, inheriting from Bird."""
    
    def __init__(self, name, age, weight_kg, wingspan, eyesight_distance):
        """Initialize an eagle with eagle-specific attributes.
        
        Args:
            name (str): The eagle's name
            age (int): The eagle's age in years
            weight_kg (float): The eagle's weight in kilograms
            wingspan (float): The eagle's wingspan in meters
            eyesight_distance (float): How far the eagle can see in kilometers
        """
        super().__init__(name, age, weight_kg, wingspan, True)  # Eagles can fly
        self.eyesight_distance = eyesight_distance
        self.species = "Aquila chrysaetos"  # Golden eagle
        
    def make_sound(self):
        """Override the make_sound method for eagles."""
        print(f"{self.name} is screeching!")
        
    def move(self):
        """Override the move method for eagles."""
        print(f"{self.name} is soaring majestically high above the mountains.")
        
    def hunt_from_above(self, prey):
        """Eagles hunt by diving from above.
        
        Args:
            prey (str): The type of animal being hunted
        """
        print(f"{self.name} spots {prey} from {self.eyesight_distance}km away and dives at high speed!")


class Snake(Reptile):
    """Class representing snakes, inheriting from Reptile."""
    
    def __init__(self, name, age, weight_kg, scale_type, is_venomous, length):
        """Initialize a snake with snake-specific attributes.
        
        Args:
            name (str): The snake's name
            age (int): The snake's age in years
            weight_kg (float): The snake's weight in kilograms
            scale_type (str): The type of scales the snake has
            is_venomous (bool): Whether the snake is venomous
            length (float): The snake's length in meters
        """
        super().__init__(name, age, weight_kg, scale_type, is_venomous)
        self.length = length
        self.species = "Python bivittatus" if not is_venomous else "Naja naja"  # Python or Cobra
        
    def make_sound(self):
        """Override the make_sound method for snakes."""
        print(f"{self.name} is hissing quietly.")
        
    def move(self):
        """Override the move method for snakes."""
        print(f"{self.name} is slithering silently through the grass.")
        
    def constrict(self, prey):
        """Non-venomous snakes like pythons constrict their prey.
        
        Args:
            prey (str): The type of animal being constricted
        """
        if not self.is_venomous:
            print(f"{self.name} wraps around {prey} and squeezes tightly.")
        else:
            print(f"{self.name} cannot constrict as it's a venomous snake.")
    
    def inject_venom(self, prey):
        """Venomous snakes inject venom into their prey.
        
        Args:
            prey (str): The type of animal being bitten
        """
        if self.is_venomous:
            print(f"{self.name} strikes {prey} with its fangs, injecting deadly venom.")
        else:
            print(f"{self.name} cannot inject venom as it's a non-venomous snake.")


# Example usage
if __name__ == "__main__":
    # Create instances of different animals
    simba = Lion("Simba", 5, 190.5, "golden", "large")
    hedwig = Eagle("Hedwig", 3, 6.2, 2.1, 3.0)
    nagini = Snake("Nagini", 8, 45.0, "smooth", True, 4.5)
    
    # Demonstrate polymorphism with the move method
    print("=== Movement Examples (Polymorphism) ===")
    simba.move()  # Lion's implementation
    hedwig.move()  # Eagle's implementation
    nagini.move()  # Snake's implementation
    
    # Demonstrate polymorphism with the make_sound method
    print("\n=== Sound Examples (Polymorphism) ===")
    simba.make_sound()  # Lion's implementation
    hedwig.make_sound()  # Eagle's implementation
    nagini.make_sound()  # Snake's implementation
    
    # Demonstrate specific methods
    print("\n=== Specific Methods ===")
    simba.hunt("zebra")
    hedwig.hunt_from_above("rabbit")
    nagini.inject_venom("mouse")
    
    # Demonstrate inherited methods
    print("\n=== Inherited Methods ===")
    simba.eat("meat")
    hedwig.sleep(2)
    nagini.bask()