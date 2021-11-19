import unittest
import main


class TestMain(unittest.TestCase):
    def setUp(self) -> None:
        print("About to Run test")

    def test_add_5(self):
        test_param = 10
        result = main.add_5(test_param)
        # * Most Important Line of test is below
        self.assertEqual(result, 15)

    def test_add_5_2(self):
        test_param = "djf"
        result = main.add_5(test_param)
        self.assertTrue(isinstance(result, ValueError))

    def test_add_5_3(self):
        test_param = ["5.0"]
        result = main.add_5(test_param)
        self.assertIsInstance(result, TypeError)

    def test_add_5_4(self):
        test_param = None
        result = main.add_5(test_param)
        self.assertEqual(result, 'Please Enter Number')


if '__name__' == '__main__':
    unittest.main()


# ->While testing you want to break things and then fix them until it becomes perfect
# -> Tests do not go into production code so please make them very descriptive
