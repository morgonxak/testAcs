import serial
port = serial.Serial("/dev/tty.usbmodem1421", 9600, timeout=0.4)
fax = open('ax.txt', 'w')
fay = open('ay.txt', 'w')
faz = open('az.txt', 'w')

ax=[]
ay=[]
az=[]

q = False
#port.open()
t=1

while t <= 100:


    temp = port.readline()
    temp = temp.decode()
    ax.append(temp)

    temp = port.readline()
    temp = temp.decode()
    ay.append(temp)

    temp = port.readline()
    temp = temp.decode()
    az.append(temp)

    t += 1

for index in ax:
    fax.write(index)

for index in ay:
    fay.write(index)

for index in az:
    faz.write(index)


port.close()
fax.close()
fay.close()