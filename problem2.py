class Person(object):

    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father


person_a = Person("User", "1", None)
person_b = Person("User", "2", person_a)


def print_depth(data):
    depth = 1
    q = [(i, depth + 1) for i in data.values() if isinstance(i, dict)]
    key = data.keys()
    for x in key:
        print(x + " " + str(depth))
    while (q):
        b = 1
        for y in q[0][0].keys():
            print(y + " " + str(depth + 1))
        b += 1
        n, depth = q.pop()
        q = q + [(i, depth + 1) for i in n.values() if isinstance(i, dict)]


a = {
    "key1": 1,
    "key2": {
        "key3": 1,
        "key4": {
            "key5": 4,
            "user": person_b,
        }
    }
}
print_depth(a)
