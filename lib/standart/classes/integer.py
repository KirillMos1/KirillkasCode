import floating, string, array, d_array, u_array

class Integer():
    def __init__(self, val):
        self.val = int(val)
    def __str__(self):
        return self.var
    def __add__(self, n):
        if isinstance(n, Integer):
            return Integer(self.val + n.val)
        elif isinstance(n, floating.Floating):
            return Floating(self.val + n.val)
        elif isinstance(n, int):
            return Integer(self.val + n)
        elif isinstance(n, float):
            return Floating(self.val + n)
        elif isinstance(n, string.String):
            raise Exception("Can`t add str to int")
        elif isinstance(n, array.Array):
            pass