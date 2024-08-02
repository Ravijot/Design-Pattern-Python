class PaymentProcessor:
    def process_payment(self, amount):
        raise NotImplementedError
        
class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        # Process credit card payment using credit card processing API
        return "Process through Credit Card"
    
class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        # Process PayPal payment using PayPal API
        return "Process through PayPal Card"
    
class ApplePayProcessor(PaymentProcessor):
    def process_payment(self, amount):
        # Process Apple Pay payment using Apple Pay API
        return "Process through PayPal Card"

class PaymentProcessorFactory:
    def get_payment_processor(self, payment_method):
        if payment_method == "credit_card":
            return CreditCardProcessor()
        elif payment_method == "paypal":
            return PayPalProcessor()
        elif payment_method == "apple_pay":
            return ApplePayProcessor()
        else:
            raise ValueError("Invalid payment method")
        
factory = PaymentProcessorFactory()


credit_card_processor = factory.get_payment_processor("credit_card")
print(credit_card_processor.process_payment(100.0))


paypal_processor = factory.get_payment_processor("paypal")
print(paypal_processor.process_payment(50.0))


apple_pay_processor = factory.get_payment_processor("apple_pay")
print(apple_pay_processor.process_payment(25.0)) 