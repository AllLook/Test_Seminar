import unittest

from Test_Seminar.Seminar_2.transport import Car, Motorcycle, Vehile


class TestIron(unittest.TestCase):

    def test_wheels_car(self):
        c1 = Car()
        m1 = Motorcycle()
        self.assertEqual(c1.num_wheels, 4)
        self.assertEqual(m1.num_wheels, 2)

    def test_speed_drive(self):
        c1 = Car()
        m1 = Motorcycle()
        self.assertEqual(c1.test_drive(), 60)
        self.assertEqual(m1.test_drive(), 75)

    def test_parking_car(self):
        c1 = Car()

        def speed_reduction() -> bool:
            temp_speed_car = c1.test_drive()
            temp_park_car = c1.park()

            while temp_speed_car > temp_park_car:
                temp_speed_car -= 1
            if temp_speed_car == temp_park_car:
                return True  # машина остановилась

        self.assertTrue(speed_reduction())

    def test_parking_motorcycle(self):
        m1 = Motorcycle()

        def speed_reduction() -> bool:
            temp_speed_motorcycle = m1.test_drive()
            temp_park_motorcycle = m1.park()

            while temp_speed_motorcycle > temp_park_motorcycle:
                temp_speed_motorcycle -= 1
            if temp_speed_motorcycle == temp_park_motorcycle:
                return True  # мотоцикл остановился

        self.assertTrue(speed_reduction())

    def test_belonging(self):
        self.assertTrue(issubclass(Car, Vehile))
