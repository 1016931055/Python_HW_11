class Incapsulator:
    def __init__(self, value=0):
        self._value = value

    def set_value(self, new_value):
        self._value = new_value

    def get_value(self):
        return self._value