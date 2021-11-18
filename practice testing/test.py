import unittest
from unittest import result
import main


class TestMain(unittest.TestCase):
    def test_add_5(self):
        test_param = 10
        result = main.add_5(test_param)
        # * Most Important Line of test is below
        self.assertEquals(15)


unittest.main()
