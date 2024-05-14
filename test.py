# from auto import Auto
# class Auto:
#     engine = "DVS"
#     wheels = 4
#
#     def __init__(self, marka):
#         self.marka = marka
#         self._speed = 0
#     # def movement(self):
#     #     self.speed += 10
#     #     return self.speed
# class Truck(Auto):
#     # engine = "hybrid"
#     def __init__(self):
#         super().__init__(self)
#         self.brand = "VOLVO"
#     # def test(self):
#     #     self.speed = 1400
#
#
# t = Truck()
# t.speed = 150
# print(t.speed)


class Hello:
    hello = "hello"
    _hello = "_hello"
    __hello = "__hello"

    def __init__(self):
        self.world = 'world'
        self._world = '_world'
        self.__world = '__world'

class Hi(Hello):
    def printer(self):
        print(self.hello)
        print(self._hello)
        # print(self.__hello)
        print(self.world)
        print(self._world )
        # print(self.__world)
h = Hi()
h.printer()