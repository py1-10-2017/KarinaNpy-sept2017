class MathDojo(object):
    def __init__(self):
        self.result = 0

    def add(self, *args):
        self.result += args
        return self
