"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self,start):
        """Initializes the value that will be returned, the variable that will be increased with each new serial number
        generation, and the variable that will hold the starting value, respectively."""
        self.starter = start
        self.counter = start
        self.start_value=start

    def generate(self):
        """Generates and returns the next serial number"""
        self.starter=self.counter
        self.counter+=1
        return self.starter
    
    def reset(self):
        """Resets the value that will be returned and the varibale that will be increased
        with each new serial number to the starting value"""
        self.starter = self.start_value
        self.counter = self.start_value
        

        
