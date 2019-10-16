t = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
cache = t[0]
t.pop(0)
t.append(cache)
print(t)
