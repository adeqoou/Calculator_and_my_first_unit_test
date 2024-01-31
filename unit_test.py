import unittest
from addtest import(
    add_test,
    second_test,
    third_test,
    forth_test)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(add_test(),12)

    def test_something2(self):
        self.assertEqual(second_test(), 52)

    def test_something3(self):
        self.assertEqual(third_test(), 48)

    def test_something4(self):
        self.assertEqual(forth_test(), 66)


if __name__ == '__main__':

    unittest.main()
