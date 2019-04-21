import Control_Module_Comm.serial_interface as serial_interface

log = 1


class instruction_manager():
    def __init__(self):
        self.serial_interface = serial_interface.serial_interface()

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
            if log: print("send test successful")
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
            line = line[4:len(line) - 5]
            line = line.split("\\x")
            return line
        return 0

    def send_live_stream_request(self, module, channel1, channel2):
        self.serial_interface.send_byte(b'\x88')
        info = str(module) + str(channel1) + str(channel2)
        self.serial_interface.send_string(info)
        line = self.serial_interface.listen()
        line = line.strip(b'\r\n')
        if line == b'\x88':
            if log: print("send live stream request successful")

    """
    instruction to request all data. sends a single byte for instruction
    the byte in hexadecimal is x86
    """

    def send_request_all_data(self):
        self.serial_interface.send_instruction(b'\x86')
        line = self.serial_interface.listen()
        line = line.strip(b'\r\n')
        if line == b'\x86':
            if log:
                print("request all data successful")
            while not line == b'\xFF\xFF\xFF\xFF\xFF\xFF\r\n':
                # store the data somehow
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
            if log: print("request live bytes successful")
            line = self.serial_interface.listen()
            line = line.strip(b'\r\n')
            if log: print("line is", line)
            return line
        return 0

    """
    request the gps data as a string. still needs post processing.
    returns a string formatted a certain way.
    format pending.
    """

    def send_gps_data_request(self):
        self.serial_interface.send_instruction(b'\x89')
        line = self.serial_interface.listen()
        line = line.strip(b'\r\n')
        if line == b'\x89':
            if log: print("gps data request successful")
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
            if log: print("gps sync request instruction successful")
            return 1
        return 0

    def send_diagnose_request(self):
        self.serial_interface.send_instruction(b'\x8B')
        line = self.serial_interface.listen()
        line = line.strip(b'\r\n')
        if line == b'\x8B':
            if log: print("diagnose request successful")
            line = self.serial_interface.listen()
            line = line.strip(b'\r\n')
            if log: print("line is", line)
            return line
        return 0

    def send_request_status(self):
        self.serial_interface.send_instruction(b'\x83')
        line = self.serial_interface.listen()
        line = line.strip(b'\r\n')
        status = [0, 0, 0]
        if line == b'\x83':
            if log: print("diagnose request successful")
            line = self.serial_interface.listen()
            line = line.strip(b'\r\n')
            line = str(line)
            line = line.strip("b'")
            if log: print("line is", line)
            line = line.split("\\x")
            if log: print("line split gives = ", line)
            status[0] = int(line[1])
            status[1] = int(line[2])
            status[2] = int(line[3])
            if log: print("instruction status = " + str(status))
            return status
        return 0

    def send_request_configuration_validity(self):
        self.serial_interface.send_instruction(b'\x8C')
        line = self.serial_interface.listen()
        line = line.strip(b'\r\n')
        if line == b'\x8C':
            if log: print("diagnose request successful")
            line = self.serial_interface.listen()
            line = line.strip(b'\r\n')
            if log: print("line is", line)
            return line
        return 0

    """
    sampling frequency
    cutoff frequency
    gain
    duration
    """

    def send_recording_parameters(self, sfrequency, cutoff, gain, duration, start_delay, sensors_selected, name,
                                  location):
        if log: print("entered send recording parameters")
        self.serial_interface.send_byte(b'\x85')
        if log: print("sent byte of instruction")
        duration = self.fix_duration(duration)
        start_delay = self.fix_duration(start_delay)
        if log:
            print("sent byte and fixed duration")
            print("sfrequency type is " + str(type(sfrequency)))
        self.serial_interface.send_byte(bytes([int(sfrequency)]))
        if log: print("sent sampling frequency")
        # send cut off
        self.serial_interface.send_byte(bytes([int(cutoff)]))
        # send gain
        self.serial_interface.send_byte(bytes([int(gain)]))
        # send duration
        self.serial_interface.send_byte(bytes([int(duration[0])]))
        self.serial_interface.send_byte(bytes([int(duration[1])]))
        self.serial_interface.send_byte(bytes([int(duration[2])]))
        self.serial_interface.send_byte(bytes([int(duration[3])]))
        # send start time delay
        self.serial_interface.send_byte(bytes([int(start_delay[0])]))
        self.serial_interface.send_byte(bytes([int(start_delay[1])]))
        self.serial_interface.send_byte(bytes([int(start_delay[2])]))
        self.serial_interface.send_byte(bytes([int(start_delay[3])]))
        # send sensors selected
        self.serial_interface.send_byte(bytes([int(sensors_selected[0])]))
        self.serial_interface.send_byte(bytes([int(sensors_selected[1])]))
        self.serial_interface.send_byte(bytes([int(sensors_selected[2])]))
        self.serial_interface.send_byte(bytes([int(sensors_selected[3])]))
        # send name
        for a in name:
            self.serial_interface.send_string_bytes(a)

        # send comma delimiter
        self.serial_interface.send_string_bytes(",")
        # send localization
        for a in location:
            self.serial_interface.send_string_bytes(a)
        # send final comma delimeter
        self.serial_interface.send_string_bytes(",")
        # finish transmission, and then wait for answer
        self.serial_interface.send_end_byte()

        if log: print("sent whole instruction")
        line = self.serial_interface.listen()
        line = line.strip(b'\r\n')
        if line == b'\x85':
            if log: print("sent recording parameters succesful")
            # line = self.serial_interface.listen()
            # if log: print("line is-", line)
            # line = line.strip(b'\r\n')
            # if log: print("got past strip")
            # line = line.split(",")
            if log: print("got past split")
            if log: print("line is", line)
            return 1
        return 0

    def fix_duration(self, duration):
        if log: print("entered fix duration")
        dur = str(duration)
        new_duration = dur
        if log: print("duration is " + new_duration)
        a = int(len(new_duration))
        if log: print("length is " + str(a))
        index = 4 - a
        if log: print("duration is " + new_duration + " index is " + str(index))
        if log: print("got to for loop in fix duration")
        while index > 0:
            new_duration = "0" + new_duration
            print("new_duration is " + new_duration)
            index = index - 1
        return new_duration

    def send_cancel_request(self):
        self.serial_interface.send_instruction(b'\xFF')
        line = self.serial_interface.listen()
        line = line.strip(b'\r\n')
        if line == b'\xFF':
            if log: print("send cancel successful")
            return 1
        return 0
