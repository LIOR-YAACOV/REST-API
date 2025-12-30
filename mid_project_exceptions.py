class IPAddrException(Exception):   
    def __init__(self, ip_addr):
        super().__init__()
        self._ip_addr = ip_addr
    
    def getIPAddr(self):
        return self._ip_addr 
    
    def __str__(self):
        return f"Error: given input: {self.getIPAddr()} is not a legal IP address"

class InvalidInput(Exception):
    def __init__(self, value, category):
        super().__init__()
        self._value = value
        self._category = category
    
    def getValue(self):
        return self._value
    
    def getCategory(self):
        return self._category
    
    def __str__(self):
        return f"Error: given input: {self.getValue()}, is not a valid value for a {self.getCategory()}"

class PortNumException(Exception):   
    def __init__(self, port):
        super().__init__()
        self._port= port
    
    def getPort(self):
        return self._port
    
    def __str__(self):
        return f"Error: given input: {self.getPort()}, is not a legal port"

class OptionException(Exception):   
    def __init__(self, option):
        super().__init__()
        self._option = option
    
    def getOption(self):
        return self._option
    
    def __str__(self):
        return f"Error: given input: {self.getOption()}, is not a legal option"