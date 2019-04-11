import serial_interface

log = 0
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
        if line == b'\x80':
            if log: print("send test succesful")
            return 1
        return 0
        
    """
    requests configuration
    """
    def send_request_configuration(self):
        self.serial_interface.send_instruction(b'\x81')
        line = self.serial_interface.listen()
        line = line.strip(b'\r\n')
        if line == b'\x81':
            if log: print("send request configuration succesful")
            line = self.serial_interface.listen()
            line = line.strip(b'\r\n')
            return line
        return 0

    """
    send an instruction byte to request start 
    """
    def send_request_start(self):
        self.serial_interface.send_instruction(b'\x82')
        line = self.serial_interface.listen()
        line = line.strip(b'\r\n')
        if line == b'\x82':
            if log: print("send request start succesful")
            return 1
        return 0
    
    """
    this is for requesting the number of modules that the device has connected at any one time. it returns 
    """
    def send_request_number_of_mods_connected(self):
        self.serial_interface.send_instruction(b'\x84')
        line = self.serial_interface.listen()
        line = line.strip(b'\r\n')
        if line == b'\x84':
            if log: print("send modules connected succesful")
            line = self.serial_interface.listen()
            line = str(line)
            line = line[4:len(line)-5]
            line = line.split("\\x")
            return line
        return 0
    """    
    def send_live_stream_request(self, module, channel1, channel2):
        self.serial_interface.send_byte(b'\x88')
        info = str(module) + str(channel1) + str(channel2)
        self.serial_interface.send_string(info)
        line = self.serial_interface.listen()
        line = line.strip(b'\r\n')
        if line == b'\x88':
            if log: print("send live stream request succesful")
            
    """
    """
    instruction to request all data. sends a single byte for instruction
    the byte in hexadecimla is x86
    """
    def send_request_all_data(self):
        self.serial_interface.send_instruction(b'\x86')
        line = self.serial_interface.listen()
        line = line.strip(b'\r\n')
        if line == b'\x86':
            if log: 
                print("request all data succesful")
            while not line == b'\xFF\xFF\xFF\xFF\xFF\xFF\r\n':
                #store the data somehow
                if log:
                    print("line in all data is: " + str(line))
                line = self.serial_interface.listen()
            return 1
        return 0

    """
    must be called while visualize is active. as in in a while loop.
    """
    def send_request_live_bytes(self):
        self.serial_interface.send_instruction(b'\x88')
        line = self.serial_interface.listen()
        line = line.strip(b'\r\n')
        if line == b'\x88':
            if log: print("request live bytes succesful")
            line = self.serial_interface.listen()
            line = line.strip(b'\r\n')
            if log: print("line is", line)
            return line
        return 0
            
    """
    request the gps data as a string. still needs post processing.
    returns a string formated a certain way.
    format pending.
    """
    def send_gps_data_request(self):
        self.serial_interface.send_instruction(b'\x89')
        line = self.serial_interface.listen()
        line = line.strip(b'\r\n')
        if line == b'\x89':
            if log: print("gps data request succesful")
            line = self.serial_interface.listen()
            line = line.strip(b'\r\n')
            if log: print("line is", line)
            return line
        return 0
            
    """
    send gps sync request. It uses the devices internal gps to sync the local RTC
    byte is 8A
    """
    def send_gps_sync_request(self):
        self.serial_interface.send_instruction(b'\x8A')
        line = self.serial_interface.listen()
        line = line.strip(b'\r\n')
        if line == b'\x8A':
            if log: print("gps sync request instruction succesful")
            return 1
        return 0
            
    def send_diagnose_request(self):
        self.serial_interface.send_instruction(b'\x8B')
        line = self.serial_interface.listen()
        line = line.strip(b'\r\n')
        if line == b'\x8B':
            if log: print("diagnose request succesful")
            line = self.serial_interface.listen()
            line = line.strip(b'\r\n')
            if log: print("line is", line)
            return line
        return 0
        
    def send_request_status(self):
        self.serial_interface.send_instruction(b'\x83')
        line = self.serial_interface.listen()
        line = line.strip(b'\r\n')
        if line == b'\x83':
            if log: print("diagnose request succesful")
            line = self.serial_interface.listen()
            line = line.strip(b'\r\n')
            if log: print("line is", line)
            return line
        return 0
        
    def send_request_configuration_validity(self):
        self.serial_interface.send_instruction(b'\x8C')
        line = self.serial_interface.listen()
        line = line.strip(b'\r\n')
        if line == b'\x8C':
            if log: print("diagnose request succesful")
            line = self.serial_interface.listen()
            line = line.strip(b'\r\n')
            if log: print("line is", line)
            return line
        return 0
    
    def send_cancel_request(self):
        self.serial_interface.send_instruction(b'\xFF')
        line = self.serial_interface.listen()
        line = line.strip(b'\r\n')
        if line == b'\xFF':
            if log: print("send cancel succesful")
            return 1
        return 0