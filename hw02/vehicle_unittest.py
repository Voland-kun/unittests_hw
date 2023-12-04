import unittest
from car import Car
from motorcycle import Motorcycle


class VehicleTest(unittest.TestCase):
    def setUp(self):
        self.car = Car("ZiL", "GAZ-21", 1965)
        self.moto = Motorcycle("IMZ-Ural", "Gear-UP", 2022)

    def test_car_instance_check(self):
        self.assertIsInstance(self.car, Car)

    def car_wheels_check(self):
        self.assertEqual(self.car.get_num_wheels(), 4)

    def moto_wheels_check(self):
        self.assertEqual(self.moto.get_num_wheels(), 2)

    def car_speed_check(self):
        self.car.test_drive()
        self.assertEqual(self.car.get_speed(), 60)

    def moto_speed_check(self):
        self.moto.test_drive()
        self.assertEqual(self.moto.get_speed(), 75)

    def car_parking_check(self):
        self.car.test_drive()
        self.car.park()
        self.assertEqual(self.car.get_speed(), 0)

    def moto_parking_check(self):
        self.moto.test_drive()
        self.moto.park()
        self.assertEqual(self.moto.get_speed(), 0)


if __name__ == "__main__":
    unittest.main()
