import Control_Module_Comm.serial_interface as serial_interface

log = 0


class instruction_manager():
    def __init__(self, port):
        self.serial_interface = serial_interface.serial_interface(port)

    def send_set_configuration(self, string):
        """
        function to set configuration.
        :param: string with configuration
        sends an instruction byte to know what it must do, and then the configuration as a string
        """
        self.serial_interface.send_byte(b'\x80')  # 128
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
        """
        requests configuration
        """
        self.serial_interface.send_instruction(b'\x81') # 129
        line = self.serial_interface.listen()
        line = line.strip(b'\r\n')
        if line == b'\x81':
            if log: print("send request configuration succesful")
            line = self.serial_interface.listen()
            line = line.strip(b'\r\n')
            return line
        return 0

    def send_request_start(self):
        """
        send an instruction byte to request start
        """
        self.serial_interface.send_instruction(b'\x82')
        line = self.serial_interface.listen()
        line = line.strip(b'\r\n')
        while not line == b'\x82':
            if log: print("send request start succesful")
            self.serial_interface.send_instruction(b'\x82')
            line = self.serial_interface.listen()
            line = line.strip(b'\r\n')
            if not line == b'\x82':
                continue
            return 1
        return 0

    def send_request_number_of_mods_connected(self):
        """
        this is for requesting the number of modules that the device has connected at any one time. it returns
        """
        self.serial_interface.send_instruction(b'\x84') # 132
        line = self.serial_interface.listen()
        line = line.strip(b'\r\n')
        if line == b'\x84':
            if log: print("send modules connected succesful")
            line = self.serial_interface.listen()
            line = str(line)
            line = line[4:len(line) - 5]
            line = line.split("\\x")
            count = 0
            for i in line:
                line[count] = int(i)
                count = count + 1
            return line
        return [-1, -1, -1, -1, -1, -1, -1, -1]

    def send_live_stream_request(self, module, channel1, channel2):
        self.serial_interface.send_byte(b'\x88')  # 136
        info = str(module) + str(channel1) + str(channel2)
        self.serial_interface.send_string(info)
        line = self.serial_interface.listen()
        line = line.strip(b'\r\n')
        if line == b'\x88':
            if log: print("send live stream request successful")

    def send_request_all_data(self):
        """
        instruction to request all data. sends a single byte for instruction
        the byte in hexadecimal is x86
        """
        self.serial_interface.send_instruction(b'\x86') # 134
        line = self.serial_interface.listen()
        line = line.strip(b'\r\n')
        line = str(line)
        line = line[2:len(line)-5]
        if log:
            print("request all data successful")
        while not line == '\xAA\xBB\xAA\xBB\r\n':
            # store the data somehow
            if log:
                print("line in all data is: " + str(line))
            line = self.serial_interface.listen()
        return 0

    def send_request_data(self, daq):
        self.serial_interface.send_byte(b'\x87') # 135
        self.serial_interface.send_instruction(bytes([daq]))
        line = self.serial_interface.listen()
        line = str(line)
        line = line[2:len(line) - 5]
        print("line is = ", line)
        if line == '\\x87':
            if log:
                print("line is " + str(line))
                print("request daq data successful")

            line1 = self.serial_interface.listen_file()
            if log:
                print("entered lines")
                print(line1)
            data = self.organize_data(line1)

            return data
        return 0

    def organize_data(self, data):
        pow_comp = pow(2, 23) - 1
        pow_sub = pow(2, 24)
        length = len(data)

        if log: print("length is ", length)

        array = []
        array.append([])
        array.append([])
        array.append([])
        array.append([])
        next_sensor = [1, 0, 0, 0]
        count = 0
        count_imp = 0

        while count < 20:
            if data[count_imp] == 67:
                count_imp = count_imp - 11
                break
            count_imp += 1
            count += 1
        count = 0
        erased = 0

        for i in range(0, int(length - 3), 3):
            if count >= 400:
                pass
            elif erased < 4:  # Erase first 4 bytes to compensate for alignment bytes.
                erased += 1
            else:
                if isinstance(data[count_imp], int) and isinstance(data[count_imp + 1], int) and isinstance(
                        data[count_imp + 2], int):
                    # if True:
                    bits = bytes([data[count_imp]]) + bytes([data[count_imp + 1]]) + bytes([data[count_imp + 2]])
                    print("count_imp", count_imp, "bits =", bits)
                    num = int.from_bytes(bits, byteorder='big')
                    if num > pow_comp:
                        num = num - pow_sub

                    if next_sensor[0]:
                        array[0].append(num)
                        next_sensor[0] = 0
                        next_sensor[1] = 1
                    elif next_sensor[1]:
                        array[1].append(num)
                        next_sensor[1] = 0
                        next_sensor[2] = 1
                    elif next_sensor[2]:
                        array[2].append(num)
                        next_sensor[2] = 0
                        next_sensor[3] = 1
                    elif next_sensor[3]:
                        array[3].append(num)
                        next_sensor[3] = 0
                        next_sensor[0] = 1
                count_imp += 3
            if count == 403:
                count_imp = count_imp + 11
                count = 3
            count += 1

        array2 = []
        for a in array:
            b = a[1:len(a)]
            array2.append(b)
        return array2

    def send_request_live_bytes(self):
        """
        must be called while visualize is active. as in in a while loop.
        """
        self.serial_interface.send_instruction(b'\x88')  # 136?
        line = self.serial_interface.listen()
        line = line.strip(b'\r\n')
        if line == b'\x88':
            if log: print("request live bytes successful")
            line = self.serial_interface.listen()
            line = line.strip(b'\r\n')
            if log: print("line is", line)
            return line
        return 0

    def send_gps_data_request(self):
        """
        request the gps data as a string. still needs post processing.
        returns a string formatted a certain way.
        returns a string formatted a certain way.
        format pending.
        """
        self.serial_interface.send_instruction(b'\x89') # 137
        line = self.serial_interface.listen()
        line = line.strip(b'\r\n')
        if line == b'\x89':
            if log: print("gps data request successful")
            line = self.serial_interface.listen()
            line = line.strip(b'\r\n')
            line = str(line)
            if log: print("line is", line)
            return line
        return "0"

    def send_gps_sync_request(self):
        """
        send gps sync request. It uses the devices internal gps to sync the local RTC
        byte is 8A
        """
        self.serial_interface.send_instruction(b'\x8A')  # 138
        line = self.serial_interface.listen()
        line = line.strip(b'\r\n')
        if line == b'\x8A':
            if log: print("gps sync request instruction successful")
            return 1
        return 0

    def send_diagnose_request(self):
        self.serial_interface.send_instruction(b'\x8B') # 139
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
        self.serial_interface.send_instruction(b'\x83') # 131
        line = self.serial_interface.listen()
        line = line.strip(b'\r\n')
        if log: print('Received ' + str(line) + 'in send request status')
        status = []
        # while line != b'\x83':
        #     print(line)
        #     line = self.serial_interface.listen()
        #     if log: print("still in while")
        if line == b'\x83':
            if log: print("diagnose request successful")
            line = self.serial_interface.listen()
            line = line.strip(b'\r\n')
            line = str(line)
            line = line.strip("b'")
            if log: print("line is", line)
            line = line.split("\\x")
            if log: print("line split gives = ", line)
            status.append(int(0))  # Recorded
            status.append(int(line[2])) # Stored
            status.append(int(line[3]))# gps_synched
            if log: print("instruction status = " + str(status))
            return status
        return [-1, -1, -1]

    def send_request_configuration_validity(self):
        self.serial_interface.send_instruction(b'\x8C')  # 140
        line = self.serial_interface.listen()
        line = line.strip(b'\r\n')
        if line == b'\x8C':
            if log: print("diagnose request successful")
            line = self.serial_interface.listen()
            line = line.strip(b'\r\n')
            if log: print("line is", line)
            return line
        return 0

    def send_recording_parameters(self, sfrequency, cutoff, gain, duration, start_delay, store_data_sd, sensor_enable, name, location):
        """
        Possible Error if sensor_enables is all zeros.

        :param sfrequency: Sampling Frequency.
        :param cutoff: Cutoff Frequency.
        :param gain: Signal Gain.
        :param duration: Test Duration.
        :param start_delay: Delay to begin recording.
        :param store_data_sd: Indicates if data should be saved in SD card.
        :param sensor_enable: Binary List of Sensors User has selected.
        :param name: Test Name.
        :param location: Test Location.
        :return:
        """
        if log: print("entered send recording parameters")
        self.serial_interface.send_byte(b'\x85')  # 133
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
        self.serial_interface.send_byte(bytes([int(store_data_sd[0])]))
        self.serial_interface.send_byte(bytes([int(store_data_sd[1])]))
        self.serial_interface.send_byte(bytes([int(store_data_sd[2])]))
        self.serial_interface.send_byte(bytes([int(store_data_sd[3])]))
        # send sensor enabled
        for i in sensor_enable:
            self.serial_interface.send_byte(bytes([i]))
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
        self.serial_interface.send_instruction(b'\xFF')  # 255
        line = self.serial_interface.listen()
        line = line.strip(b'\r\n')
        if line == b'\xFF':
            if log: print("send cancel successful")
            return 1
        return 0
