class GrandParents:
    gladness = 100
    age = 80

    def __init__(self, name_gp, name_gm):
        self.name_gp = name_gp
        self.name_gm = name_gm

    def printer(self):
        print("class GrandParents", GrandParents.gladness, GrandParents.age, self.name_gp, self.name_gm)


class Parents(GrandParents):
    work = True

    def __init__(self, satiety, name_gp, name_gm):
        super().__init__(name_gp, name_gm)
        self.satiety = satiety


class Children(Parents):
    age = 15

    def __init__(self, toys, satiety, name_gp, name_gm):
        super().__init__(satiety, name_gp, name_gm)
        self.toys = toys

    def printer(self):
        super().printer()
        print(f"Age {Children.age} {self.toys}")


ch1 = Children("Ball", 80, "Ivan", "Anna")
print(ch1.toys)
print(ch1.satiety)
print(ch1.gladness)
print(ch1.name_gm)
ch1.printer()
