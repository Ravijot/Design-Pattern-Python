from abc import ABC,abstractmethod
#Define Product 
class Pizza:
    def __init__(self):
        self.ingredients = []
        
    def add_ingredients(self, ingredient):
        self.ingredients.append(ingredient)
        
    def list_ingredients(self) -> None:
        print(f"Pizza Ingridients : {','.join(self.ingredients)}")
        
#Define Builder Interface
class PizzaBuilder(ABC):
    @property
    @abstractmethod
    def pizza(self) -> None:
        pass

    @abstractmethod
    def produce_dough(self):
        pass
    
    @abstractmethod
    def produce_sauce(self):
        pass
    
    @abstractmethod
    def produce_topping(self):
        pass
    
    @abstractmethod
    def produce_cheese(self):
        pass

class VegPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.reset()
        
    def reset(self) -> None:
        self._pizza = Pizza()
        
    @property
    def pizza(self) -> Pizza:
        return self._pizza
    
    def produce_dough(self) -> None:
        self.pizza.add_ingredients("Whole White Dough")
    
    def produce_sauce(self) -> None:
        self.pizza.add_ingredients("Tomato Sauce")
        
    def produce_topping(self) -> None:
        self.pizza.add_ingredients("Onions, Mushrooms, Olives")
    
    def produce_cheese(self) -> None:
        self.pizza.add_ingredients("Mozzarella Cheese")
    
class MeatPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.reset()
    
    def reset(self)-> None:
        self._pizza = Pizza()
    
    @property
    def pizza(self) -> Pizza:
        return self._pizza
    
    def produce_dough(self) -> None:
        self.pizza.add_ingredients("Regular Dough")
    
    def produce_sauce(self) -> None:
        self.pizza.add_ingredients("Barbecue Sauce")
    
    def produce_topping(self) -> None:
        self.pizza.add_ingredients("Pepperoni, Sausage, Bacon")
    
    def produce_cheese(self) -> None:
        self.pizza.add_ingredients("Cheddar Cheese")
        
#Create the Dictator 
class PizzaDirector:
    def __init__(self):
        self._builder = None
    
    @property
    def builder(self) -> PizzaBuilder:
        return self._builder

    @builder.setter
    def builder(self, builder: PizzaBuilder) -> None:
        self._builder = builder
        
    def build_vegetarian_pizza(self) -> None:
        self.builder.produce_dough()
        self.builder.produce_sauce()
        self.builder.produce_topping()
        self.builder.produce_cheese()
        
    def build_meat_pizza(self) -> None:
        self.builder.produce_dough()
        self.builder.produce_sauce()
        self.builder.produce_topping()
        self.builder.produce_cheese()
    
if __name__ == "__main__":
    director = PizzaDirector()

    print("Vegetarian Pizza: ")
    veg_builder = VegPizzaBuilder()
    director.builder = veg_builder
    director.build_vegetarian_pizza()
    veg_builder.pizza.list_ingredients()

    print("\n")

    print("Meat Lovers Pizza: ")
    meat_builder = MeatPizzaBuilder()
    director.builder = meat_builder
    director.build_meat_pizza()
    meat_builder.pizza.list_ingredients()

    print("\n")

    print("Custom Pizza: ")
    custom_builder = VegPizzaBuilder()
    custom_builder.produce_dough()
    custom_builder.produce_sauce()
    custom_builder.produce_cheese()
    custom_builder.pizza.list_ingredients()