import unittest

from problem1 import print_depth


class TestDepth(unittest.TestCase):
    def test_depth(self):
        a = {
            "key1": 1,
            "key2": {
                "key3": 1,
                "key4": {
                    "key5": 4,
                    "key6": 6,
                    "key7": 7,
                    "key8": {
                        "key9": 8,
                        "key10": {
                            "key11": 8
                        }
                    },

                }
            }
        }

        print_depth(a)


if __name__ == '__main__':
    unittest.main()
