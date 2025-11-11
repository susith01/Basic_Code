class PowerFinder:
    def __init__(self, a, b):  
        self.a = int(a)
        self.b = int(b)
    def find_last_digit(self):
        d = self.a ** self.b
        return str(d)[-1]
obj = PowerFinder("3", "10")
print(obj.find_last_digit())
