import serial
port = serial.Serial("/dev/tty.usbmodem1421", 9600)
while True:
    print(port.readline())