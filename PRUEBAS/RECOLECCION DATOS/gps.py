
import serial

SerialPort = None

SerialPort = serial.Serial('COM5', 9600)

CP = []
BD = 0
BD = SerialPort.readline().decode().split(",")
CP = BD
SerialPort.close()
print(type(CP), CP)


