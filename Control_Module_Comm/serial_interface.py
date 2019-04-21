import serial
import time

log = 0


class serial_interface():
    global ser

    def __init__(self, port):
        """
        :exception : Throws serial.serialutil.SerialException when not connected.
        """
        # FIXME still crashes later on because:
        #  line 79, in send_instruction
        #  self.ser.write(bytes(byte))
        #  AttributeError: 'serial_interface' object has no attribute 'ser'
        self.port = port
        self.ser = serial.Serial(
            port=self.port,
            baudrate=230400,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=2)
        print("connected to: " + self.ser.portstr)


    """
    listen will block until it receives a tranmission ending with
    bytes \r\n and then it will return it to it's caller. it would be advantegous to use it as a thread. 
    """

    def listen(self):
        ser = self.ser
        line = ser.readline()
        if log: print("entered listen")
        while not line:
            line = ser.readline()
            continue
        if log: print("received: " + str(line))
        if log: print("left listen")
        return line

    """
    send a string of data. this function will automatically close the data being sent. 
    """

    def send_string(self, string):
        st = bytes(string, 'ascii')
        self.ser.write(st)

        # send stop byte
        self.ser.write(b'\r')

    """
    send string byte with no ending
    """
    def send_string_bytes(self, byte):
        st = bytes(byte, 'ascii')
        self.ser.write(st)

    """
    send ending byte
    """
    def send_end_byte(self):
        self.ser.write(b'\r')


    """
    send byte is important to be able to send instructions as bytes, that are not on the ascii table. 
    """

    def send_byte(self, byte):
        self.ser.write(bytes(byte))
        if log == 1:
            print("byte is " + str(bytes(byte)))


    def send_instruction(self, byte):
        """
        I need a byte that does not end the stream of bytes being sent.
        """
        try:
            self.ser.write(bytes(byte))
            if log == 1: print("byte is " + str(bytes(byte)))
            self.ser.write(b'\r')
        except AttributeError:
            print('The Root Error was Already Handled.')
            print('This error is caused by handling the Serial Failed to Connect Error.')
