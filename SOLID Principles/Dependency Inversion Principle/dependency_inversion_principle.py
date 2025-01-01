"""
Dependency Inversion Principle

It states that that high-level modules should not depend on low-level modules. Both should depend on abstractions.
Additionally, abstractions should not depend on details; details should depend on abstractions.
"""


class MySQLDatabase:
    """
    A class representing a MySQL database.

    This class handles data storage and retrieval using MySQL.
    """

    def connect(self):
        print("Connecting to MySQL database...")

    def save_data(self, data: str):
        print(f"Saving {data} to MySQL database.")


class DataProcessor:
    """
    A class for processing data and saving it to a database.

    This class violates the Dependency Inversion Principle because it directly
    depends on a specific implementation (MySQLDatabase).
    """

    def __init__(self):
        self.database = MySQLDatabase()

    def process_data(self, data: str):
        """
        Process and save data to the database.

        Args:
            data (str): The data to be processed and saved.
        """
        print("Processing data...")
        self.database.connect()
        self.database.save_data(data)


# Example Usage
processor = DataProcessor()
processor.process_data("Sample Data")

"""
The above code violates Dependency Inversion Principle as the DataProcessor class directly depends on the MySQLDatabase
class, which makes it inflexible. If we want to switch to a different database (e.g., PostgreSQL), we must modify the
DataProcessor class as well.

We can apply dependency-inversion principle to the above classes as follows
"""

from abc import ABC, abstractmethod

class Database(ABC):
    """
    Abstract base class for a database.

    This abstraction ensures that high-level modules depend on an interface,
    not on specific implementations.
    """
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def save_data(self, data: str):
        pass


class MySQLDatabase(Database):
    """
    A class representing a MySQL database.
    """
    def connect(self):
        print("Connecting to MySQL database...")

    def save_data(self, data: str):
        print(f"Saving {data} to MySQL database.")


class PostgreSQLDatabase(Database):
    """
    A class representing a PostgreSQL database.
    """
    def connect(self):
        print("Connecting to PostgreSQL database...")

    def save_data(self, data: str):
        print(f"Saving {data} to PostgreSQL database.")


class DataProcessor:
    """
    A class for processing data and saving it to a database.

    This class follows the Dependency Inversion Principle by depending
    on an abstraction (Database) rather than a specific implementation.
    """
    def __init__(self, database: Database):
        self.database = database

    def process_data(self, data: str):
        """
        Process and save data to the database.

        Args:
            data (str): The data to be processed and saved.
        """
        print("Processing data...")
        self.database.connect()
        self.database.save_data(data)


# Example Usage
mysql_db = MySQLDatabase()
postgres_db = PostgreSQLDatabase()

processor1 = DataProcessor(mysql_db)
processor1.process_data("Sample Data 1")

processor2 = DataProcessor(postgres_db)
processor2.process_data("Sample Data 2")

"""
DataProcessor now depends on the abstraction Database rather than concrete implementations. The database implementation
(e.g., MySQLDatabase, PostgreSQLDatabase) can be easily swapped without modifying DataProcessor. This makes the code
more flexible and easier to maintain.

The above code now conforms to the DIP principle.
"""
