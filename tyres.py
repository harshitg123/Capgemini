
lis = []

for i in range(int(input())):

    car, bike = input().split(" ")

    car = int(car)
    bike = int(bike)

    tyres = car*4 + bike*2
    lis.append(tyres)

for j in lis:
    print(j)