"""Interface Segregation Principle (ISP).
Clients should not be forced to depend on interfaces they do not use.
Instead of one fat interface, many small interfaces are better.
"""

from abc import abstractmethod


class Machine:
    """Base class for all machines."""

    def print(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError


class MultiFunctionPrinter(Machine):
    """Multi function printer that can print, fax and scan."""

    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass


class OldFashionedPrinter(Machine):
    """Old fashioned printer that can only print and can't fax or scan."""

    def print(self, document):
        # OK
        pass

    def fax(self, document):
        # not OK, but we can't change the base class
        pass

    def scan(self, document):
        raise NotImplementedError("Old fashioned printer can't scan")


class Printer:
    @abstractmethod
    def print(self, document):
        pass


class Scanner:
    @abstractmethod
    def scan(self, document):
        pass


class Fax:
    @abstractmethod
    def fax(self, document):
        pass


class PrinterImpl(Printer):
    def print(self, document):
        print(document)


class ScannerImpl(Printer, Scanner):
    def print(self, document):
        print(f"Printing {document}")

    def scan(self, document):
        print(f"Scanning {document}")


class FaxImpl(Printer, Fax):
    def print(self, document):
        print(f"Printing {document}")

    def fax(self, document):
        print(f"Faxing {document}")


class MultiFunctionDevice(Printer, Scanner, Fax):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass

    @abstractmethod
    def fax(self, document):
        pass


class MultiFunctionDeviceImpl(MultiFunctionDevice):
    def __init__(self, printer: Printer, scanner: Scanner, fax: Fax):
        self._printer = printer
        self._scanner = scanner
        self._fax = fax

    def print(self, document):
        self._printer.print(document)

    def scan(self, document):
        self._scanner.scan(document)

    def fax(self, document):
        self._fax.fax(document)


def main():
    printer = PrinterImpl()
    scanner = ScannerImpl()
    fax = FaxImpl()
    multi_function_device = MultiFunctionDeviceImpl(printer, scanner, fax)
    multi_function_device.print("Hello, world!")
    multi_function_device.scan("Hello, world!")
    multi_function_device.fax("Hello, world!")


if __name__ == "__main__":
    main()
