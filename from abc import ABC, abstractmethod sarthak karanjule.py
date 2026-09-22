from abc import ABC, abstractmethod

# ---------------- Strategy Interface ----------------
class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# ---------------- Concrete Strategies ----------------
class CreditCardPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")


class UPIPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI.")


class PayPalPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid ₹{amount} using PayPal.")


# ---------------- Context Class ----------------
class PaymentProcessor:

    def __init__(self, strategy):
        self.strategy = strategy

    # Change payment strategy dynamically
    def set_strategy(self, strategy):
        self.strategy = strategy

    # Process payment
    def process_payment(self, amount):
        self.strategy.pay(amount)
