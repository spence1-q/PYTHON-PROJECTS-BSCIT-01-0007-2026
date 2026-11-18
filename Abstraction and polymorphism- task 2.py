# Create a parent class named Vehicle.
class Vehicle:
  # Define a method named calculateFare().
  def calculateFare(self, distance):
    pass


# Create a class named Bus that implements calculateFare() using Fare = Distance * 50
class Bus(Vehicle):

  def calculateFare(self, distance):
    return distance * 50


# Create a class named Taxi that implements calculateFare() using Fare = Distance * 100
class Taxi(Vehicle):

  def calculateFare(self, distance):
    return distance * 100


# Create one Bus object and one Taxi object.
bus_obj = Bus()
taxi_obj = Taxi()

# Pass a distance of 10 kilometres to both objects.
distance = 10
bus_fare = bus_obj.calculateFare(distance)
taxi_fare = taxi_obj.calculateFare(distance)

# vii. Display the calculated fare for each vehicle.
print(f"Bus Fare for {distance} km: {bus_fare}")
print(f"Taxi Fare for {distance} km: {taxi_fare}")

# Calling the same calculateFare() method on different objects (bus_obj and taxi_obj) produces different results because both subclasses override the parent class method with their own tailored logic (distance * 50 for the bus versus distance * 100 for the taxi). This dynamic method dispatch is a core manifestation of runtime polymorphism.