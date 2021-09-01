l1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
l2 = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]

zipped = zip(l2, l1)

for _,i in sorted(zipped):
    print(i, end=" ")