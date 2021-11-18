import unittest
import main


class TestMain(unittest.TestCase):
    def test_add_5(self):
        test_param = 0
        result = main.add_5(test_param)
        self.assertEqual(result, 'Please Enter Number')


if '__name__' == '__main__':
    unittest.main()

# -> Can also run all test simultaneously by running : python -m unittest in CLI
