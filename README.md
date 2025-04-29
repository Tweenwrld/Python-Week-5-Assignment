# Object-Oriented Programming Demonstrations

This repository contains two Python programs demonstrating key object-oriented programming (OOP) concepts: inheritance, encapsulation, constructors, and polymorphism.

## Overview

These activities were designed to showcase practical implementations of OOP principles in Python through engaging examples:

1. **Animal Kingdom Classes**: A hierarchical class structure modeling different animal types with shared and specialized behaviors
2. **Vehicle Polymorphism Challenge**: A demonstration of polymorphism through different vehicle types that implement the same methods in unique ways

## Activity 1: Animal Kingdom Classes

### Description

This program models an animal kingdom hierarchy with base and derived classes:

- `Animal`: The base class with common attributes and methods
- `Mammal`, `Bird`, `Reptile`: Mid-level classes that inherit from `Animal`
- `Lion`, `Eagle`, `Snake`: Specialized classes that inherit from their respective animal types

### Key Concepts Demonstrated

- **Inheritance**: Classes inherit attributes and methods from parent classes
- **Encapsulation**: Data and associated methods are bundled within classes
- **Constructors**: Each class uses `__init__` to initialize object attributes
- **Polymorphism**: Methods like `move()` and `make_sound()` behave differently in each animal class
- **Method Overriding**: Child classes override parent methods to provide specialized behavior

### Usage

```python
# Example usage
simba = Lion("Simba", 5, 190.5, "golden", "large")
hedwig = Eagle("Hedwig", 3, 6.2, 2.1, 3.0)
nagini = Snake("Nagini", 8, 45.0, "smooth", True, 4.5)

# Demonstrate polymorphism
simba.move()    # Lion's movement
hedwig.move()   # Eagle's movement
nagini.move()   # Snake's movement

# Call specific methods
simba.hunt("zebra")
hedwig.hunt_from_above("rabbit")
nagini.inject_venom("mouse")
```

## Activity 2: Vehicle Polymorphism Challenge

### Description

This program implements different types of vehicles with a common interface but unique implementations:

- `Vehicle`: Base class with common functionality
- `Car`, `Motorcycle`, `Boat`, `Plane`: Specialized vehicle types

### Key Concepts Demonstrated

- **Polymorphism**: The `move()` method is implemented differently by each vehicle class
- **Inheritance**: All vehicles inherit common attributes and methods from the `Vehicle` class
- **Encapsulation**: Vehicle-specific attributes and behaviors are properly encapsulated
- **Method Overriding**: Each vehicle type provides its own implementation of shared methods

### Usage

```python
# Create different vehicles
tesla = Car("Tesla", "Model S", 2023, "red", "electric", 4)
harley = Motorcycle("Harley-Davidson", "Street Glide", 2022, "black", 1868, False)
boeing = Plane("Boeing", "747", 2020, "blue and white", 45000, 4)

# Start vehicles
tesla.start()
harley.start()
boeing.start()

# Demonstrate polymorphism
tesla.move()    # "The red Tesla Model S is driving on the road. 🚗"
harley.move()   # "The 1868cc Harley-Davidson Street Glide is zooming through traffic. 🏍️"
boeing.move()   # Shows plane needs to take off first

# Demonstrate specific methods
tesla.honk()
harley.pop_wheelie()
boeing.take_off()
```

## Learning Objectives

By studying and experimenting with these programs, you will:

1. Understand how to design class hierarchies in Python
2. See practical examples of inheritance and method overriding
3. Learn how polymorphism enables flexible and extensible code design
4. Practice implementing constructors to initialize object state
5. Explore encapsulation by bundling data with methods that operate on that data

## How to Run

1. Each activity is contained in its own Python file
2. Run either program directly with Python:
   ```
   python animal_kingdom_classes.py
   python vehicle_polymorphism.py
   ```
3. The example code at the bottom of each file will demonstrate the key concepts

## Extension Ideas

1. Add new animal or vehicle types to the hierarchy
2. Add additional methods to existing classes
3. Create a simple text-based game using these class hierarchies
4. Implement additional OOP concepts like multiple inheritance or abstract classes
5. Add error handling with custom exceptions

## Requirements

- Python 3.6 or higher
- No external dependencies required# Object-Oriented Programming Demonstrations

This repository contains two Python programs demonstrating key object-oriented programming (OOP) concepts: inheritance, encapsulation, constructors, and polymorphism.

## Overview

These activities were designed to showcase practical implementations of OOP principles in Python through engaging examples:

1. **Animal Kingdom Classes**: A hierarchical class structure modeling different animal types with shared and specialized behaviors
2. **Vehicle Polymorphism Challenge**: A demonstration of polymorphism through different vehicle types that implement the same methods in unique ways

## Activity 1: Animal Kingdom Classes

### Description

This program models an animal kingdom hierarchy with base and derived classes:

- `Animal`: The base class with common attributes and methods
- `Mammal`, `Bird`, `Reptile`: Mid-level classes that inherit from `Animal`
- `Lion`, `Eagle`, `Snake`: Specialized classes that inherit from their respective animal types

### Key Concepts Demonstrated

- **Inheritance**: Classes inherit attributes and methods from parent classes
- **Encapsulation**: Data and associated methods are bundled within classes
- **Constructors**: Each class uses `__init__` to initialize object attributes
- **Polymorphism**: Methods like `move()` and `make_sound()` behave differently in each animal class
- **Method Overriding**: Child classes override parent methods to provide specialized behavior

### Usage

```python
# Example usage
simba = Lion("Simba", 5, 190.5, "golden", "large")
hedwig = Eagle("Hedwig", 3, 6.2, 2.1, 3.0)
nagini = Snake("Nagini", 8, 45.0, "smooth", True, 4.5)

# Demonstrate polymorphism
simba.move()    # Lion's movement
hedwig.move()   # Eagle's movement
nagini.move()   # Snake's movement

# Call specific methods
simba.hunt("zebra")
hedwig.hunt_from_above("rabbit")
nagini.inject_venom("mouse")
```

## Activity 2: Vehicle Polymorphism Challenge

### Description

This program implements different types of vehicles with a common interface but unique implementations:

- `Vehicle`: Base class with common functionality
- `Car`, `Motorcycle`, `Boat`, `Plane`: Specialized vehicle types

### Key Concepts Demonstrated

- **Polymorphism**: The `move()` method is implemented differently by each vehicle class
- **Inheritance**: All vehicles inherit common attributes and methods from the `Vehicle` class
- **Encapsulation**: Vehicle-specific attributes and behaviors are properly encapsulated
- **Method Overriding**: Each vehicle type provides its own implementation of shared methods

### Usage

```python
# Create different vehicles
tesla = Car("Tesla", "Model S", 2023, "red", "electric", 4)
harley = Motorcycle("Harley-Davidson", "Street Glide", 2022, "black", 1868, False)
boeing = Plane("Boeing", "747", 2020, "blue and white", 45000, 4)

# Start vehicles
tesla.start()
harley.start()
boeing.start()

# Demonstrate polymorphism
tesla.move()    # "The red Tesla Model S is driving on the road. 🚗"
harley.move()   # "The 1868cc Harley-Davidson Street Glide is zooming through traffic. 🏍️"
boeing.move()   # Shows plane needs to take off first

# Demonstrate specific methods
tesla.honk()
harley.pop_wheelie()
boeing.take_off()
```

## Learning Objectives

By studying and experimenting with these programs, you will:

1. Understand how to design class hierarchies in Python
2. See practical examples of inheritance and method overriding
3. Learn how polymorphism enables flexible and extensible code design
4. Practice implementing constructors to initialize object state
5. Explore encapsulation by bundling data with methods that operate on that data

## How to Run

1. Each activity is contained in its own Python file
2. Run either program directly with Python:
   ```
   python Animal_kingdom_classes.py
   python Vehicle_polymorphism_challenge.py
   ```
3. The example code at the bottom of each file will demonstrate the key concepts

## Requirements

- Python 3.6 or higher
- No external dependencies required