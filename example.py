class X:
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self.value

x = X(42)
print(x.value)