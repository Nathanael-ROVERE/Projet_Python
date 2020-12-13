import os

def icon_path():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\icons\\'
def model_path():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\models\\'


def frange(x, y, jump=1.0):
    '''Range for floats.'''
    i = 0.0
    x = float(x)  # Prevent yielding integers.
    x0 = x
    epsilon = jump / 2.0
    yield x  # yield always first value
    while x + epsilon < y:
        i += 1.0
        x = x0 + i * jump
        yield x


class Switch:
    """define a switch statement
    """
    def __init__(self, value):
        self.value = value

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        return False  # Allows a traceback to occur

    def __call__(self, *values):
        return self.value in values


class Callback(object):
    """create easy usavle callback for buttons
    """
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def __call__(self, *args):
        return self.func(*self.args, **self.kwargs)
