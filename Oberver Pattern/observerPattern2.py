from abc import ABC,abstractmethod
class Observer(ABC):
    @abstractmethod
    def update(self, temperatur : float,humidity : float, pressure : float):
        pass

class DisplayDevice(ABC):
    @abstractmethod
    def display(self):
        pass

class CurrentConditionDisplay(Observer, DisplayDevice):
    def __init__(self):
        self.temperature = 0
        self.humidity = 0
        
    def update(self , temperatue : float, humidity : float, pressure : float):
        self.temperature = temperatue
        self.humidity = humidity
        self.display()
        
    def display(self):
        print(f"Current conditions: {self.temperature}°C, {self.humidity}%")

class ForecastDisplay(Observer,DisplayDevice):
    def __init__(self):
        self.pressure = 0
        
    def update(self, temperature : float, humidity : float, pressure : float):
        self.pressure = pressure
        self.display()
        
    def display(self):
        print(f"Forecast: {self.pressure} hPa")

class Subject(ABC):
    def __init__(self):
        self._observers = []
    
    def attach(self, observer : Observer):
        self._observers.append(observer)
    
    def detach(self, observer : Observer):
        self._observers.remove(observer)
    
    def notify(self, temperature : float, humidity : float, pressure : float):
        for observer in self._observers:
            observer.update(temperature, humidity, pressure)

class WeatherStation(Subject):
    def __init__(self):
        super().__init__()
        self._temperature = 0
        self._humidity = 0
        self._pressure = 0
        
    @property
    def temperature(self):
        return self._temperature
    
    @temperature.setter
    def temperature(self, value):
        self._temperature = value
        self.measurements_changed()
        
    @property
    def pressure(self):
        return self._pressure

    @pressure.setter
    def pressure(self, value):
        self._pressure = value
        self.measurements_changed()
    
    def measurements_changed(self):
        self.notify(self._temperature, self._humidity, self._pressure)
        
# Example Usage
weather_station = WeatherStation()

current_display = CurrentConditionDisplay()
forecast_display = ForecastDisplay()

weather_station.attach(current_display)
weather_station.attach(forecast_display)

weather_station.temperature = 22.5

weather_station.pressure = 1013.25 
weather_station.humidity = 100

weather_station.temperature = 30.0

weather_station.humidity = 80
weather_station.pressure = 120

# Output:
weather_station.detach(current_display)