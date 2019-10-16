# 1チーム4名
# 1チームに情報系が2名とその他2名
# 全チームパターンの配列を生成

c = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
o = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
t = []
tl = []
tll = []

for k in range(8):
    for j in range(8):
        for i in range(8):
            if i % 2 == 0:
                t.append(c[i])
                t.append(c[i+1])
                t.append(o[i])
                t.append(o[i+1])
                tl.append(t)
                t = []
        tll.append(tl)
        tl = []

        cache_c = c[0]
        c.pop(0)
        c.append(cache_c)
    cache_o = o[0]
    o.pop(0)
    o.append(cache_o)
