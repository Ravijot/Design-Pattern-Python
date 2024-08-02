# Adaptee
class EuropeanPlug:
    def plug_in_eu_socket(self):
        return "220V from European socket"

# Target Interface
class USASocket:
    def provide_power(self):
        pass

# Adapter
class EuropeanToUSAAdapter(USASocket):
    def __init__(self, european_plug):
        self.european_plug = european_plug

    def provide_power(self):
        # Adapter translates the request to the European plug
        return self.european_plug.plug_in_eu_socket()

# Client code
def main():
    european_plug = EuropeanPlug()
    adapter = EuropeanToUSAAdapter(european_plug)
    print(adapter.provide_power())  # Output: 220V from European socket

if __name__ == "__main__":
    main()
