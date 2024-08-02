from abc import ABC,abstractmethod

#Abstract Products
class AbstractCar(ABC):
    @abstractmethod
    def drive(self):
        pass
    
class AbstractEngine(ABC):
    @abstractmethod
    def start(self):
        pass
    
#Concrete Products
class ElectricCar(AbstractCar):
    def drive(self):
        return "Driving an electric car"
    
class PetrolCar(AbstractCar):
    def drive(self):
        return "Driving a petrol car"
    
class ElectricEngine(AbstractEngine):
    def start(self):
        return "Starting an electric engine"
    
class PetrolEngine(AbstractEngine):
    def start(self):
        return "Starting a petrol engine"
    
#Abstract Factory
class AbstractFactory(ABC):
    @abstractmethod
    def create_car(self):
        pass
    @abstractmethod
    def create_engine(self):
        pass
    
#Concrete Factories
class ElectricCarFactory(ABC):
    def create_car(self):
        return ElectricCar()
    
    def create_engine(self):
        return ElectricEngine()
    
class PetrolCarFactory(ABC):
    def create_car(self):
        return PetrolCar()
    
    def create_engine(self):
        return PetrolEngine()

def client(factory : AbstractFactory):
    car = factory.create_car()
    engine = factory.create_engine()
    print(engine.start())
    print(car.drive())
    
    
if __name__=='__main__':
    print("Bought Electric Car from electric Car Factory")
    client(ElectricCarFactory())
    
    print("Bought Petrol Car from Petrol Car Factory")
    client(PetrolCarFactory())
    