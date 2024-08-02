class Database:
    def __init__(self):
        self.connect()

    def connect(self):
        print("Connecting to the database...")

    def query(self, sql):
        print(f"Executing query: {sql}")

# Proxy class
class DatabaseProxy:
    def __init__(self):
        self.database = None

    def connect(self):
        if self.database is None:
            self.database = Database()

    def query(self, sql):
        if self.database is None:
            self.connect()
        self.database.query(sql)

# Client code
if __name__ == "__main__":
    db_proxy = DatabaseProxy()

    # The first query will trigger the connection to the database
    db_proxy.query("SELECT * FROM users")

    # Subsequent queries will use the existing connection
    db_proxy.query("SELECT * FROM orders")