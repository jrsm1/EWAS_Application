import serial

ser = serial.Serial(
    port='COM6',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
        timeout=1)

print("connected to: " + ser.portstr)
count=1

ser.write(b'hola\r')
print("---test end---")