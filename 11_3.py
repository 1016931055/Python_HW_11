class SpyingNumber:
    global_counter = 0

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"SpyingNumber({self.value})"

    def __add__(self, other):
        if isinstance(other, (int, float)):
            other = SpyingNumber(other)
        SpyingNumber.global_counter += 1
        return SpyingNumber(self.value + other.value)

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            other = SpyingNumber(other)
        SpyingNumber.global_counter += 1
        return SpyingNumber(self.value - other.value)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            other = SpyingNumber(other)
        SpyingNumber.global_counter += 1
        return SpyingNumber(self.value * other.value)

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            other = SpyingNumber(other)
        SpyingNumber.global_counter += 1
        return SpyingNumber(self.value / other.value)

    @staticmethod
    def get_global_counter():
        return SpyingNumber.global_counter

    @staticmethod
    def reset_global_counter():
        SpyingNumber.global_counter = 0