"""
Interface Segregation Principle

It states that no client should be forced to depend on methods it does not use. Instead of creating a large,
general-purpose interface, we should create smaller, more specific interfaces for different client needs.
"""


class Printer:
    """
    A base class representing a printer.

    This class violates the Interface Segregation Principle because it forces all subclasses
    to implement methods that may not be relevant to their functionality.
    """

    def print_document(self, content: str):
        """
        Print the content of a document.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    def scan_document(self):
        """
        Scan a document and return the scanned content.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    def fax_document(self):
        """
        Fax a document to a specified number.
        """
        raise NotImplementedError("Subclasses must implement this method.")

class AllInOnePrinter(Printer):
    """
    A printer that supports printing, scanning, and faxing.
    """

    def print_document(self, content: str):
        return f"Printing: {content}"

    def scan_document(self):
        return "Scanning document..."

    def fax_document(self):
        return "Faxing document..."

class BasicPrinter(Printer):
    """
    A basic printer that only supports printing.

    This violates the Interface Segregation Principle because it is forced to implement
    irrelevant methods like scan_document and fax_document.
    """

    def print_document(self, content: str):
        return f"Printing: {content}"

    def scan_document(self):
        raise NotImplementedError("Basic printers cannot scan.")

    def fax_document(self):
        raise NotImplementedError("Basic printers cannot fax.")

# Example Usage
printers = [AllInOnePrinter(), BasicPrinter()]

for printer in printers:
    print(printer.print_document("Hello World"))
    print(printer.scan_document())  # Fails for BasicPrinter
    print(printer.fax_document())  # Fails for BasicPrinter

"""
The above code violates the Interface Segregation Principle because the BasicPrinter class is forced to implement
irrelevant methods like scan_document and fax_document.

We can apply interface segregation principle to the above class as follows
"""

from abc import ABC, abstractmethod

class Printable(ABC):
    """
    An interface for printers that support printing.
    """

    @abstractmethod
    def print_document(self, content: str):
        """
        Print the content of a document.
        """
        pass

class Scannable(ABC):
    """
    An interface for printers that support scanning.
    """

    @abstractmethod
    def scan_document(self):
        """
        Scan a document and return the scanned content.
        """
        pass

class Faxable(ABC):
    """
    An interface for printers that support faxing.
    """

    @abstractmethod
    def fax_document(self):
        """
        Fax a document to a specified number.
        """
        pass

class AllInOnePrinter(Printable, Scannable, Faxable):
    """
    A printer that supports printing, scanning, and faxing.
    """

    def print_document(self, content: str):
        return f"Printing: {content}"

    def scan_document(self):
        return "Scanning document..."

    def fax_document(self):
        return "Faxing document..."

class BasicPrinter(Printable):
    """
    A basic printer that only supports printing.
    """

    def print_document(self, content: str):
        return f"Printing: {content}"

# Example Usage
printers = [AllInOnePrinter(), BasicPrinter()]

for printer in printers:
    print(printer.print_document("Hello World"))
    if isinstance(printer, Scannable):
        print(printer.scan_document())
    if isinstance(printer, Faxable):
        print(printer.fax_document())

"""
In this corrected version, we adhere to the Interface Segregation Principle by separating the Printable,
Scannable, and Faxable interfaces, we ensure that each printer class implements only the methods
relevant to its functionality.

The above code now conforms to the ISP principle.
"""
