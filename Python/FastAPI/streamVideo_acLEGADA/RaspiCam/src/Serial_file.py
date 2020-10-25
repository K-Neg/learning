import serial
import serial.tools.list_ports
import time
from threading import Thread


class SerialCom(Thread):
    def __init__(self, serial_port, baudrate):
        Thread.__init__(self, name="SerialCom")
        self.serial_port = serial_port
        self.baudrate = baudrate
        self.running = True
        self._terminate = False
        self.msg = None

        try:
            self.serial = serial.Serial(
                serial_port, baudrate, timeout=0, write_timeout=0.01
            )

        except Exception as inst:
            self.running = False
            print(inst)

    def parameters(self, interface):
        self.interface = interface

    def send_msg(self, msg_send):
        try:
            self.serial.write(msg_send.encode())

        except Exception as inst:
            print(inst)

    def terminate(self):
        self.serial.close()
        self._terminate = True
        self.running = False

    def resume(self):
        self.running = True

    def pause(self):
        self.running = False

    def run(self):
        while not self._terminate:
            while self.running:
                ports = list(serial.tools.list_ports.comports())

                if len(ports) > 0:
                    flag_port = False
                    for p in ports:
                        if self.serial_port in p:
                            flag_port = True
                            break

                    if flag_port == False:
                        self.serial.close()
                        # print("disconnected")
                        self.running = False
                else:
                    # print("disconnected")
                    self.running = False

                try:
                    if self.serial.inWaiting() > 0:
                        self.msg = self.serial.readline().decode("utf-8").strip()
                        print(self.msg)

                except:
                    continue

            while not self.running:
                try:
                    self.serial = serial.Serial(
                        self.serial_port, self.baudrate, timeout=0, write_timeout=0.01
                    )
                    self.running = True
                    # print("connected")
                except:
                    continue