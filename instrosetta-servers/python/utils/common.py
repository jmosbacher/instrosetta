
def test_connected(f):
    def wrapped(self, *args, **kwargs):
        if not self.connected:
            raise ConnectionError("Device not connected.")
        return f(self, *args, **kwargs)
    return wrapped
