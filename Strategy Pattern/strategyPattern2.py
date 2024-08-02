from abc import ABC, abstractmethod

class TransportationSrategy(ABC):
    @abstractmethod
    def travel(self, start : str, destination : str):
        pass

class CarStrategy(TransportationSrategy):
    def travel(self, start : str, destination : str):
        print(f"Travelling from {start} to {destination} by Car")
        
class BusStrategy(TransportationSrategy):
    def travel(self, start : str, destination : str):
        print(f"Travelling from {start} to {destination} by Bus")
 
class BicycleStrategy(TransportationSrategy):
    def travel(self, start: str, destination: str):
        print(f"Traveling from {start} to {destination} by bicycle")
       
class TravelPlanner:
    def __init__(self, strategy : TransportationSrategy):
        self._strategy = strategy
    
    def set_strategy(self, strategy : TransportationSrategy):
        self._strategy = strategy
    
    def plan_trip(self, start : str, destination : str):
        self._strategy.travel(start, destination)

if __name__ == '__main__':
    carStrategy = CarStrategy()
    busStrategy = BusStrategy()
    bicycleStrategy = BicycleStrategy()
    
    travel_planner = TravelPlanner(carStrategy)
    travel_planner.plan_trip("Home", "Office")
    
    travel_planner.set_strategy(busStrategy)
    travel_planner.plan_trip("Home", "School")
    
    travel_planner.set_strategy(bicycleStrategy)
    travel_planner.plan_trip("Home", "Park")