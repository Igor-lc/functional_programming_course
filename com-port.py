import serial
from serial.tools import list_ports
import sys

# Знайти доступні COM порти
available_ports = list_ports.comports()
port_name = None
for port in available_ports:
    if "COM" in port.device:
        port_name = port.device
        break

if port_name is None:
    print("COM порт не знайдено")
    sys.exit()

port = serial.Serial(port_name, baudrate=115200, timeout=1)

virtual_port_name = port.name
print("Віртуальний COM порт:", virtual_port_name)

data = "Hello, COM port!"
port.write(data.encode())

port.close()
