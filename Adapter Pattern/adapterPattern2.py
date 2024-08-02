# Target Interface
class PaymentProcessor:
    def process_payment(self, amount):
        pass

# Adaptee 1
class Stripe:
    def charge(self, amount):
        return f"Charging {amount} using Stripe"

# Adaptee 2
class PayPal:
    def make_payment(self, amount):
        return f"Paying {amount} using PayPal"

# Adapter for Stripe
class StripeAdapter(PaymentProcessor):
    def __init__(self, stripe):
        self.stripe = stripe

    def process_payment(self, amount):
        return self.stripe.charge(amount)

# Adapter for PayPal
class PayPalAdapter(PaymentProcessor):
    def __init__(self, paypal):
        self.paypal = paypal

    def process_payment(self, amount):
        return self.paypal.make_payment(amount)

# Client code
def main():
    stripe = Stripe()
    paypal = PayPal()

    stripe_adapter = StripeAdapter(stripe)
    paypal_adapter = PayPalAdapter(paypal)

    print(stripe_adapter.process_payment(100))  # Output: Charging 100 using Stripe
    print(paypal_adapter.process_payment(200))  # Output: Paying 200 using PayPal

if __name__ == "__main__":
    main()
