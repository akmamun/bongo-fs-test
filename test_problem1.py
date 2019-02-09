import unittest
from problem1 import print_depth


class TestDepth(unittest.TestCase):

    def test_depth_one(self):
        a = {"key1": 1}

        self.assertEqual(print_depth(a), 1)

    def test_depth_two(self):
        a = {"key1": {
            "key2": 2
        }}

        self.assertEqual(print_depth(a), 2)


if __name__ == '__main__':
    unittest.main()
