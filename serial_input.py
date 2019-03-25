import serial

ser = serial.Serial(
    port='COM6',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=1)

print("connected to: " + ser.portstr)
count=1

line = ser.readline()
while not line:
    line = ser.readline()
    if line:
        print(line)
        print("----line printed-----")

ser.close()
print("end program")