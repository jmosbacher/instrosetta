import serial
import struct
import time
import ast
import enum


def test_connected(f):
    def wrapped(self, *args, **kwargs):
        if not self.connected:
            raise ConnectionError("Device not connected.")
        return f(self, *args, **kwargs)
    return wrapped

class TestableEnum(enum.Enum):
    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)

class ShutterState(TestableEnum):
    CLOSED = 0
    OPEN = 1
    AUTO = 2

class ReadoutMode(TestableEnum):
    FVB = 0
    MULTI_TRACK = 1
    RESERVED = 2
    SINGLE_TRACK = 3
    IMAGE = 4


class SolisProxy:
    """
    Connects to a proxy script running in
    Andor solis, written with Andor BASIC.
    Script must be running for communication to work.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.conn = None
        self.sio = None
        self.polling_interval = 0.2

    @test_connected
    def read(self):
        msg = self.sio.readline().strip()
        self.conn.write(f"ACK:{msg}")
        return msg

    @test_connected
    def write(self, msg):
        self.sio.flush()
        self.sio.write(f'{msg}')
        time.sleep(0.1)
        resp = self.sio.readline().strip()
        if resp != f"ACK:{msg}":
            raise ConnectionError("Message not acknowledged by peer.")
        return True

    def read_response(self, timeout):
        responses = []
        start = time.time()
        while abs(time.time()-start)<timeout:
            resp = self.read()
            if resp == "OK":
                break
            elif resp != "":
                responses.append(resp)
            else:
                time.sleep(self.polling_interval)
        else:
            raise ConnectionError("Conversation not terminated by peer.")
        if len(responses)==1:
            return responses[0]
        else:
            return responses

    def query(self, *msgs, timeout=1):
        for msg in msgs:
            self.write(msg)
        resp = self.read_response(timeout)
        return resp
        
    def save(self, path):
        self.query("CALL","SAVE", path)

    def clear_screen(self):
        self.query("CALL","CLEARSCREEN")
        
    def get_shutter_state(self):
        return self.query("GET","SHUTTER")

    def set_shutter_state(self, state: ShutterState):
        self.query("SET","SHUTTER", state.value)

    def run(self):
        self.query('CALL","RUN')

    @property
    def grating(self):
        return self.query("GET","GRATING")

    @grating.setter
    def grating(self, value):
        if value in [1, 2]:
            self.query("SET","GRATING", value)
        while True:
            if self.grating == f"{value}":
                break
            else:
                time.sleep(4)

    @property
    def wavelength(self):
        return self.query("GET","WAVELENGTH")

    @wavelength.setter
    def wavelength(self, value):
        if (2000 >= value >= 200):
            self.query("SET","WAVELENGTH", value)

    @property
    def exposure(self):
        return self.query("GET","EXPOSURE")

    @exposure.setter
    def exposure(self, value):
        self.query("SET","EXPOSURE", value)

    @property
    def slit_width(self):
        return self.query("GET","SLIT_WIDTH")

    @slit_width.setter
    def slit_width(self, value):
        if (2500 >= value >=10):
            self.query("SET","SLIT_WIDTH", value)

    def connect(self, com_port, baudrate=115200, timeout=0.2):
        self.polling_interval = timeout
        self.disconnect()
        try:
            self.conn = serial.Serial(com_port, baudrate=baudrate, timeout=timeout)
            self.sio = io.TextIOWrapper(io.BufferedRWPair(self.conn, self.conn))
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
            