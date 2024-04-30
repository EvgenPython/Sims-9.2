from random import randint


class Student:
    def __init__(self, name):
        self.name = name
        self.progress = 0
        self.gladness = 50
        self.alive = True

    def to_study(self):
        print('Time to study')
        self.progress += 1
        self.gladness -= 1

    def to_sleep(self):
        print('Time to sleep')
        self.gladness += 1
        self.progress -= 0.1

    def to_chill(self):
        print("Time to chill")
        self.progress -= 0.1
        self.gladness += 1

    def end_of_day(self):
        print(f"Gladness {self.gladness}")
        print(f"Progress {round(self.progress, 2)}")

    def is_alive(self):
        if self.progress <= -0.5:
            print("Cast out...")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression")
            self.alive = False
        elif self.progress >= 15:
            print("Passed EXTERNALLY")
            self.alive = False

    def live(self, day):
        print(f"Day {str(day):-^50}")
        live_cube = randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        self.end_of_day()
        self.is_alive()


nick = Student(name="Nick")
for day in range(1, 366):
    if nick.alive == False:
        break
    nick.live(day)
