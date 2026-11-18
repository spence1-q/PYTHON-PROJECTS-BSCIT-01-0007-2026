import math
from abc import ABC, abstractmethod


# Create an abstract class named Shape.
class Shape(ABC):

  # Define an abstract method named area().
  @abstractmethod
  def area(self):
    pass


# Create a class named Circle that inherits from Shape.
class Circle(Shape):

  def __init__(self, radius):
    self.radius = radius

  # Implement area() in Circle using Area = pi * radius^2
  def area(self):
    return math.pi * (self.radius**2)


# Create a class named Rectangle that inherits from Shape.
class Rectangle(Shape):

  def __init__(self, length, width):
    self.length = length
    self.width = width

  # Implement area() in Rectangle using Area = Length * Width
  def area(self):
    return self.length * self.width


# Create one circle object and one rectangle object.
circle_obj = Circle(7)
rectangle_obj = Rectangle(10, 5)

# Calculate and display the area of both shapes.
print(f"Circle Area: {circle_obj.area():.2f}")
print(f"Rectangle Area: {rectangle_obj.area()}")

# Polymorphism in Action: The program defines a uniform interface (area()) within the abstract base class Shape. When the area() method is invoked on circle_obj and rectangle_obj, Python dynamically determines the correct object type and executes the specific formula corresponding to that shape (Circle computes $\pi r^2$, while Rectangle computes $\text{Length} \times \text{Width}$).