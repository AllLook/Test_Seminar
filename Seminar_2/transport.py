import abc
from datetime import datetime


class Vehile(abc.ABC):
    company: str
    model: str
    speed = int
    num_wheels: int
    yearRelease: datetime.date

    def test_drive(self):
        return

    def park(self):
        return


class Car(Vehile):
    # c1 = Vehile()
    # numWheels = c1.numWheels
    # speed = c1.speed
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.num_wheels = 4
        # self.speed = 0

    def test_drive(self):
        self.speed = 60
        return self.speed

    def park(self):
        self.speed = 0
        return self.speed


class Motorcycle(Vehile):
    # c1 = Vehile()
    # numWheels = c1.numWheels
    # speed = c1.speed
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.num_wheels = 2
        # self.speed = 0

    def test_drive(self):
        self.speed = 75
        return self.speed

    def park(self):
        self.speed = 0
        return self.speed
