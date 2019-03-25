import serial_interface

log = 1
class instruction_manager():
    def init(self, listen):
        self.serial_interface = serial_interface.serial_interface()
        self.listen = listen
        
    """
    function to set configuration.
    input: string with configuration
    sends an instruction byte to know what it must do, and then the configuration as a string
    """
    def send_set_configuration(self, string):
        self.serial_interface.send_byte(b'\x80')
        self.serial_interface.send_string(string)
        line = self.serial_interface.listen()
        line = line.strip(b'\r\n')
        if line == b'\xFF':
            if log: print("send test succesful")
            return 1
        
    """
    requests configuration
    """
    def send_request_configuration(self):
        self.serial_interface.send_instruction(b'\x81')
        line = self.serial_interface.listen()
        line = line.strip(b'\r\n')
        if line == b'\xFF':
            if log: print("send request configuration succesful")
            line = self.serial_interface.listen()
            line = line.strip(b'\r\n')
    
    """
    send an instruction byte to request start 
    """
    def send_request_start(self):
        self.serial_interface.send_instruction(b'\x82')
        line = self.serial_interface.listen()
        line = line.strip(b'\r\n')
        if line == b'\xFF':
            if log: print("send request start succesful")
            return 1
    
    """
    this is for requesting the number of modules that the device has connected at any one time. it returns 
    """
    def send_request_number_of_mods_connected(self):
        self.serial_interface.send_instruction(b'\x84')
        line = self.serial_interface.listen()
        line = line.strip(b'\r\n')
        if line == b'\xFF':
            if log: print("send modules connected succesful")
            line = self.serial_interface.listen()
            line = str(line)
            line = line[4:len(line)-5]
            line = line.split("\\x")
            return line
        
    def send_live_stream_request(self, module, channel1, channel2):
        self.serial_interface.send_byte(b'\x88')
        info = str(module) + str(channel1) + str(channel2)
        self.serial_interface.send_string(info)
        line = self.serial_interface.listen()
        line = line.strip(b'\r\n')
        if line == b'\xFF':
            if log: print("send live stream request succesful")
            
    def send_cancel_request(self):
        self.serial_interface.send_instruction(b'\xFF')
        line = self.serial_interface.listen()
        line = line.strip(b'\r\n')
        if line == b'\xFF':
            if log: print("send cancel succesful")
            return 1