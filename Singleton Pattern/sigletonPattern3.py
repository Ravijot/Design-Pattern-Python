#Example with threading
import threading

class SingletonMeta(type):
    _instances = {}
    _lock = threading.Lock()  # Add a lock object to ensure thread safety

    def __call__(cls, *args, **kwargs):
        with cls._lock:  # Ensure that only one thread can create an instance at a time
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    pass

# Usage
singleton1 = Singleton()
singleton2 = Singleton()
#print(singleton1 is singleton2)  # Output: True

# Usage in a multithreaded context
def create_singleton():
    singleton = Singleton()
    print(f"Singleton instance ID: {id(singleton)}")

threads = [threading.Thread(target=create_singleton) for _ in range(10)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()