from abc import ABC, abstractmethod


# Create an abstract class named Payment.
class Payment(ABC):

  # Define an abstract method named makePayment().
  @abstractmethod
  def makePayment(self):
    pass


# Create a class named MobileMoneyPayment that inherits from Payment.
class MobileMoneyPayment(Payment):

  # Implement makePayment() in MobileMoneyPayment
  def makePayment(self):
    print("Payment made using Mobile Money")


# Create another class named CardPayment that inherits from Payment.
class CardPayment(Payment):

  # Implement makePayment() in CardPayment
  def makePayment(self):
    print("Payment made using Bank Card")


# Create objects of both classes and call makePayment().
if __name__ == "__main__":
  mobile_payment = MobileMoneyPayment()
  card_payment = CardPayment()

  mobile_payment.makePayment()
  card_payment.makePayment()

  # Abstraction: The Payment class serves as an abstract blueprint using Python's abc module. It defines the interface (makePayment()) without providing any implementation details, hiding the complexity of how each specific payment is processed and forcing subclasses to implement it.

# Polymorphism: Both MobileMoneyPayment and CardPayment implement the same method name (makePayment()), but each executes its own specific behavior when invoked. This allows different payment objects to be used interchangeably through a common interface.