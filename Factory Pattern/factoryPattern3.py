from abc import ABC, abstractmethod

# Product Interface
class Transport(ABC):
    @abstractmethod
    def deliver(self) -> str:
        pass

# Concrete Products
class Truck(Transport):
    def deliver(self) -> str:
        return "Deliver by land in a box."

class Ship(Transport):
    def deliver(self) -> str:
        return "Deliver by sea in a container."

# Creator Class
class Logistics(ABC):
    @abstractmethod
    def create_transport(self) -> Transport:
        pass

    def plan_delivery(self) -> str:
        transport = self.create_transport()
        return transport.deliver()

# Concrete Creators
class RoadLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Truck()

class SeaLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Ship()

# Client Code
def client_code(logistics: Logistics) -> None:
    print(f"Client: {logistics.plan_delivery()}")

if __name__ == "__main__":
    print("App: Launched with RoadLogistics.")
    client_code(RoadLogistics())

    print("\nApp: Launched with SeaLogistics.")
    client_code(SeaLogistics())
