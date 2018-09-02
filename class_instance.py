class MingMing:
    name = 'human'

    def __init__(self, name, age):
        self.name = name
        self.age = age


ming = MingMing("Ming", 20)
print("instance.name:", ming.name, " class.name:", MingMing.name)
MingMing.name = 'Girl'
ming.name = 'Boy'
print("class.name:", MingMing.name)
print("instance.name:", ming.name)

