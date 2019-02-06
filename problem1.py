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
            "key5": 4
        }
    }
}
print_depth(a)
