from abc import ABC,abstractmethod

#Strategy Pattern
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

#Concrete Strategy for Credit Card Payment
class CreditCardStrategy(PaymentStrategy):
    def __init__(self, name :str, card_number : str, cvv : str, expiry_date : str):
        self.name = name
        self.card_number = card_number
        self.cvv = cvv
        self.expiry_date = expiry_date
    
    def pay(self, amount : float):
        print(f"Paid {amount} using Credit Card")
        
#Concrete Strategy for PayPal Payment

class PayPalStrategy(PaymentStrategy):
    def __init__(self, email : str, password : str):
        self.email = email
        self.password = password
        
    def pay(self, amount : float):
        print(f"Paid {amount} using PayPal")
        
#Concrete Strategy for Bitcoin Payment
class BitcoinPayment(PaymentStrategy):
    def __init__(self, wallet_address : str):
        self.wallet_address = wallet_address
        
    def pay(self, amount : float):
        print(f"Paid {amount} using Bitcoin")
    
#Context
class PaymentProcessor:
    def __init__(self, payment_strategy : PaymentStrategy):
        self.payment_strategy = payment_strategy
        
    def set_strategy(self, strategy : PaymentStrategy):
        self.payment_strategy = strategy
        
    def process_payment(self, amount : float):
        self.payment_strategy.pay(amount)

if __name__ == '__main__':
    creditCardPayment = CreditCardStrategy("John","12345","425","18-08-28")
    paypalStrategy = PayPalStrategy("john@example.com","password123")
    bitcoinStrategy = BitcoinPayment("1njj579dghdu993nuuHH")
    
    paymentProcessor = PaymentProcessor(creditCardPayment)
    paymentProcessor.process_payment(100)
    
    paymentProcessor.set_strategy(paypalStrategy)
    paymentProcessor.process_payment(200)
    
    paymentProcessor.set_strategy(bitcoinStrategy)
    paymentProcessor.process_payment(300)