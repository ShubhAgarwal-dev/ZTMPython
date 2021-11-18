import unittest
import main


class TestMain(unittest.TestCase):
    def test_add_5(self):
        test_param = 10
        result = main.add_5(test_param)
        # * Most Important Line of test is below
        self.assertEqual(result, 15)

    def test_add_5_2(self):
        test_param = "djf"
        result = main.add_5(test_param)
        # * Most Important Line of test is below
        self.assertTrue(isinstance(result, ValueError))


# unittest.main()

'''
While testing you want to break things and then fix them
'''
