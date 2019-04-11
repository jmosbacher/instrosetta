import serial
import struct
import time
import ast
import enum


class ShutterState(enum.Enum):
    CLOSED = 0
    OPEN = 1
    AUTO = 2

    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)


class ReadoutMode(enum.Enum):
    FVB = 0
    MULTI_TRACK = 1
    RESERVED = 2
    SINGLE_TRACK = 3
    IMAGE = 4

    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)


class SolisProxy:
    """
    Connects to a proxy script running in
    Andor solis, written with Andor BASIC.
    Script must be running for communication to work.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.conn = None

    def read(self):
        msg = self.conn.read(200).strip().decode()
        self.conn.write(f"ACK:{msg}")
        return msg

    def write(self, msg):
        self.conn.write(f'{msg}\r'.encode())
        time.sleep(0.1)
        resp = self.conn.read(200).strip().decode()
        if resp != f"ACK:{msg}":
            raise ConnectionError("Message not acknowledged by peer.")
        return True

    def query(self, msg):
        self.write(msg)
        resp = self.read()
        term = self.read()
        if term != "OK":
            raise ConnectionError("Conversation not terminated by peer.")
        return resp

    def command(self, cmd, *args):
        self.write(cmd)
        for arg in args:
            self.write(arg)

    def save(self, path):
        self.command("CALL:SAVE", path)

    def clear_screen(self):
        self.command("CALL:CLEARSCREEN")
        
    def get_shutter_state(self):
        return self.query("GET:SHUTTER")

    def set_shutter_state(self, state: ShutterState):

        self.command("SET:SHUTTER", state.value)

    def run(self):
        self.query('CALL:RUN')

    @property
    def grating(self):
        return self.query("GET:GRATING")

    @grating.setter
    def grating(self, value):
        if value in [1, 2]:
            self.command("SET:GRATING", value)
        while True:
            if self.grating == f"{value}":
                break
            else:
                time.sleep(4)

    @property
    def wavelength(self):
        return self.query("GET:WAVELENGTH")

    @wavelength.setter
    def wavelength(self, value):
        if (2000 >= value >= 200):
            self.command("SET:WAVELENGTH", value)

    @property
    def exposure(self):
        return self.query("GET:EXPOSURE")

    @exposure.setter
    def exposure(self, value):
        self.command("SET:EXPOSURE", value)

    @property
    def slit_width(self):
        return self.query("GET:SLIT_WIDTH")

    @slit_width.setter
    def slit_width(self, value):
        if (2500 >= value >=10):
            self.command("SET:SLIT_WIDTH", value)

    def connect(self, com_port, baudrate=115200, timeout=0.2):
        self.disconnect()
        try:
            self.conn = serial.Serial(com_port, baudrate=baudrate, timeout=timeout)
        except:
            pass

    @property
    def connected(self):
        if self.conn is None:
            return False
        return self.conn.is_open
        
    def disconnect(self):
        if self.connected:
            self.conn.close()
            