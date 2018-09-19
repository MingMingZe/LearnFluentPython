from threa.enum_time import TimeUnits
from threa.my_threadpool import Waiter


def cook():
    return "saosao"


if __name__ == '__main__':
    waiters = Waiter()
    token = waiters.put_task(cook)
    menu = token.get_menu(1, time_unit=TimeUnits.S)
    print(menu)

