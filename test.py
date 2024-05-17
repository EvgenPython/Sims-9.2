from auto import Auto
class Auto:
    engine = "DVS"
    wheels = 4
    def __init__(self, accident):
        self._speed = 0
        self.accident = accident
    def movement(self):
        if self.accident != False:
            self.speed += 10
            return self.speed
class Truck(Auto):
    # engine = "hybrid"
    def __init__(self, brand):
        super().__init__(self)
        self.brand = brand
    def test(self):
        self.speed = 1400


t = Truck("Volvo")
print(t.brand)
print(t.accident)
# t.speed = 150
# print(t.speed)


# class Hello:
#     hello = "hello"
#     _hello = "_hello"
#     __hello = "__hello"
#
#     def __init__(self):
#         self.world = 'world'
#         self._world = '_world'
#         self.__world = '__world'
#
# class Hi():
#     def __init__(self,a,b):
#         self.__a = a
#
#     def __printer(self):
#         print(self.hello)
#         print(self._hello)
#         # print(self.__hello)
#         print(self.world)
#         print(self._world)
#         # print(self.__world)
# h = Hi(5,2)
# h.printer()