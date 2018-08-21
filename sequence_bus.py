from numbers import Integral


class Bus:
    def __init__(self, plate, color, passengers):
        self.plate = plate
        self.color = color
        self.passengers = passengers

    def __getitem__(self, item):
        """
        对于列表切片有两种可能一种是传入slice对象另一种是int
        保证我切出来的乘客都会是Bus类型的
        :param item:passenger
        :return: Bus
        """
        cls = type(self)
        if isinstance(item, slice):
            return cls(
                plate=self.plate,
                color=self.color,
                passengers=self.passengers
            )
        if isinstance(item, Integral):
            return cls(
                plate=self.plate,
                color=self.color,
                passengers=[self.passengers]
            )

    def __len__(self):
        return len(self.passengers)

    def __reversed__(self):
        self.passengers = self.passengers[::-1]

    def __iter__(self):
        return iter(self.passengers)

    def __contains__(self, item):
        if item in self.passengers:
            return True
        else:
            return False


if __name__ == '__main__':
    passengers = ['mingming', 'qiangqiang', 'doudou', 'maimai']
    bus = Bus("888888", "red", passengers)
    print("bus:", bus)
    front_bus = bus[:2]
    print("front_bus", front_bus, "passengers:", front_bus.passengers)
    reversed(bus)
    print("reverse bus:", bus.passengers)
    print(len(bus))
    family = []
    for person in bus:
        family.append(person)
    print("family:", family)
    if "mingming" in bus:
        print("contain is usable")
