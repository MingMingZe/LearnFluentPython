from time import time
from threa.enum_time import TimeUnits


class my_token:
    def __init__(self):
        self.menu = None

    def get_menu(self, maxtime, time_unit=TimeUnits.S):
        if time_unit is not TimeUnits.S:
            maxtime = TimeUnits.converse_time(time_unit, maxtime)
        t0 = time()
        while (self.menu is None):
            if time() - t0 >= maxtime:
                break
        return self.menu

    def set_menu(self, result):
        self.menu = result
