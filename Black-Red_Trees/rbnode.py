# KLASA WEZLA

class rbnode:
    def __init__(self, key):
        self._key = key
        self._red = False
        self._left = None
        self._right = None
        self._p = None
        self._drawn = False

    key = property(fget=lambda self: self._key)
    red = property(fget=lambda self: self._red)
    left = property(fget=lambda self: self._left)
    right = property(fget=lambda self: self._right)
    p = property(fget=lambda self: self._p)
    drawn = property(fget=lambda self: self._drawn)

    def __str__(self):
        return str(self.key)

    def __repr__(self):
        return str(self.key)
