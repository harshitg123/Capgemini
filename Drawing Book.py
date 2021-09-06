n = int(input())
p = int(input())

frontPagesCount = 0
lastPagesCount = 0

for i in range(1, n, 2):
    if i == p or i > p:
        break
    else:
        frontPagesCount = frontPagesCount + 1

for j in range(n, 1, -2):
    if j == p or j < p or (j-1 == p and n%2!=0) :
        break
    else:
        lastPagesCount = lastPagesCount + 1

if frontPagesCount < lastPagesCount:
    print(frontPagesCount)

else:
    print(lastPagesCount)
