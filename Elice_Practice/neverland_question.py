def neverland(i):
    first = i[2]
    i.remove(first)
    i.sort()
    i.insert(0,first)
    return i

queue = [30, 10, 20, 50, 40, 60]
print(neverland(queue))
