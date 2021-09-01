# n!/(n-r)!

no_of_students = int(input()) 
no_of_seates = int(input())

n = 1
d = 1

for i in range(1, no_of_students+1):

    n = n * i

for j in range(1, (no_of_students - no_of_seates)+1):

    d = d * j

print(n/d)