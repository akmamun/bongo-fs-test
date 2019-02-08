import unittest

from problem2 import Person, print_depth


class PersonTestDepth(unittest.TestCase):

    def person_test_depth(self):
        person_a = Person("User", "1", "s")
        person_b = Person("User", "2", person_a)
        a = {
            "key1": 1,
            "key2": {
                "key3": 1,
                "key4": {
                    "key5": 4,
                    "key6": {
                        "key7": 4,
                    },
                    "user": person_b,
                    "user1": person_a,
                }
            }
        }

        print_depth(a)


if __name__ == '__main__':
    unittest.main()
