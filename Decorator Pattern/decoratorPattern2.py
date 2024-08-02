class Pizza:
    """
    The base Pizza interface defines operations that can be altered by
    decorators.
    """
    def cost(self) -> float:
        pass

    def description(self) -> str:
        pass
class PlainPizza(Pizza):
    """
    Concrete Components provide default implementations of the operations. There
    might be several variations of these classes.
    """
    def cost(self) -> float:
        return 5.0

    def description(self) -> str:
        return "Plain Pizza"
class PizzaDecorator(Pizza):
    """
    The base Decorator class follows the same interface as the other components.
    The primary purpose of this class is to define the wrapping interface for
    all concrete decorators. The default implementation of the wrapping code
    might include a field for storing a wrapped component and the means to
    initialize it.
    """
    def __init__(self, pizza: Pizza) -> None:
        self._pizza = pizza

    def cost(self) -> float:
        return self._pizza.cost()

    def description(self) -> str:
        return self._pizza.description()
class CheeseDecorator(PizzaDecorator):
    """
    Concrete Decorators call the wrapped object and alter its result in some
    way.
    """
    def cost(self) -> float:
        return self._pizza.cost() + 1.0

    def description(self) -> str:
        return f"{self._pizza.description()}, Cheese"

class PepperoniDecorator(PizzaDecorator):
    def cost(self) -> float:
        return self._pizza.cost() + 1.5

    def description(self) -> str:
        return f"{self._pizza.description()}, Pepperoni"

class OlivesDecorator(PizzaDecorator):
    def cost(self) -> float:
        return self._pizza.cost() + 0.75

    def description(self) -> str:
        return f"{self._pizza.description()}, Olives"

def client_code(pizza: Pizza) -> None:
    """
    The client code works with all objects using the Pizza interface. This
    way it can stay independent of the concrete classes of components it works
    with.
    """
    print(f"Description: {pizza.description()}")
    print(f"Cost: ${pizza.cost():.2f}")

if __name__ == "__main__":
    # Create a plain pizza
    plain_pizza = PlainPizza()
    
    # Add cheese topping
    cheese_pizza = CheeseDecorator(plain_pizza)
    
    # Add pepperoni topping
    pepperoni_pizza = PepperoniDecorator(cheese_pizza)
    
    # Add olives topping
    fully_loaded_pizza = OlivesDecorator(pepperoni_pizza)
    
    # Print the description and cost of the fully loaded pizza
    print("Client: Ordering a fully loaded pizza:")
    client_code(fully_loaded_pizza)
