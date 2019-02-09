class Person(object):

    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father


person_a = Person("User", "1", None)
person_b = Person("User", "2", person_a)
extra_counter = 0


def print_depth(data):
    depth = 1
    q = [(i, depth + 1) for i in data.values() if isinstance(i, dict)]
    key = data.keys()
    # print(key)
    # print(q)
    for x in key:
        global extra_counter
        extra_counter = 0
        if (not isinstance(data[x], Person)):
            print(x + " " + str(depth))
        else:
            print(x + " " + str(depth))

            def recurse(person, a, counter):
                if not isinstance(person, Person):
                    print(a + " " + str(counter))
                else:
                    global extra_counter
                    extra_counter += 1
                    if (extra_counter > 1):
                        print(a + " " + str(counter))
                    counter_global = counter + 1
                    person_first_name = person.first_name
                    person_last_name = person.last_name
                    person_father = person.father
                    recurse(person_first_name, "first_name", counter_global)
                    recurse(person_last_name, "last_name", counter_global)
                    recurse(person_father, "father", counter_global)

            recurse(data[x], None, 1)

    while (q):
        b = 1
        dicts = q[0][0]
        for y in dicts.keys():
            new_depth = depth + 1
            extra_counter = 0
            if not isinstance(dicts[y], Person):
                print(y + " " + str(new_depth))
            else:
                print(y + " " + str(new_depth))

                def recurse(person, a, counter):
                    if not isinstance(person, Person):

                        print(a + " " + str(counter))
                    else:
                        global extra_counter
                        extra_counter += 1
                        if (extra_counter > 1):
                            print(a + " " + str(counter))
                        counter_global = counter + 1
                        person_first_name = person.first_name
                        person_last_name = person.last_name
                        person_father = person.father
                        recurse(person_first_name, "first_name", counter_global)
                        recurse(person_last_name, "last_name", counter_global)
                        recurse(person_father, "father", counter_global)

                recurse(dicts[y], None, new_depth)
        b += 1
        n, depth = q.pop()
        q = q + [(i, depth + 1) for i in n.values() if isinstance(i, dict)]
    return depth


a = {
    "key1": 1,
    "key2": {
        "key3": 1,
        "key4": {
            "key5": 4,
            "user": person_b,
        }
    },
}
print_depth(a)
