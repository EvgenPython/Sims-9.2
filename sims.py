from random import randint, choice


class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.job = job
        self.home = home
        self.car = car
        self.satiety = 50

    def get_home(self):
        self.home = House()
    def get_car(self):
        self.car = Auto(brand_list)
    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)
    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
        self.satiety += 5
        self.home.food -= 5
    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 5
    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = "fuel"
            else:
                self.to_repair()
                return
        if manage == "fuel":
            print("I bought fuel")
            self.car.fuel = 100
            self.money -= 100
        elif manage == "food":
            print("Bought food")
            self.money -= 20
            self.home.food += 50
        elif manage == "delicacies":
            print("I'm happy!")
            self.gladness += 5
            self.money -= 10
            self.satiety += 2
    def days_indexes(self, day):
        # ------------Day 1------------
        day = f"Today the {day} of {self.name}'s life"
        print(f"Day {day:-^50}")


    def to_repair(self):
        pass # Home Work
    def chill(self):
        pass  # Home Work
    def clean_home(self):
        pass  # Home Work

class House:
    def __init__(self):
        self.food = 0
        self.mess = 0


class Auto:
    def __init__(self, brand_list):
        self.brand = choice(list(brand_list)) # BMW
        self.fuel = brand_list[self.brand]['fuel']
        self.strength = brand_list[self.brand]['strength']
        self.consumption = brand_list[self.brand]["consumption"]
    def drive(self):
        if self.strength > 0 and self.fuel > self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("The car cannot move")
            return False

class Job:
    def __init__(self, job_list):
        self.job = choice(tuple(job_list))
        self.salary = job_list[self.job]['salary']
        self.gladness_less = job_list[self.job]['gladness_less']

brand_list = {
    "BMW": {'fuel': 10, "strength": 80, "consumption": 20},
    "AUDI": {'fuel': 30, "strength": 100, "consumption": 15},
    "OPEL": {'fuel': 40, "strength": 50, "consumption": 10},
}
job_list = {
    "Developer Java": {'salary': 50, "gladness_less": 10},
    "Developer Python": {'salary': 30, "gladness_less": 20},
    "Developer C++": {'salary': 60, "gladness_less": 5},
}
