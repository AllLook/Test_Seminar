import unittest

from Test_Seminar.Seminar_3.even_odd import even_odd_num, numberInInterval


class TestNum(unittest.TestCase):
    def test_even_odd(self):
        self.assertTrue(even_odd_num(6))

    def numberInInterval(self):
        self.assertTrue(numberInInterval(30))
