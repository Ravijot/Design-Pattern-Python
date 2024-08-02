class Singleton:
    _instance = None
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
if __name__ == "__main__":
    s1 = Singleton().get_instance()
    s2 = Singleton().get_instance()
    if s1 is s2:
        print("Same instance")
    else:
        print("Different instances")