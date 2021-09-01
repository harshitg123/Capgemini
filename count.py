
# very Important for Frequency calculation

n = int(input())
lis = [int(i) for i in input().split(" ")]

dic = {}

for i in lis:

    if i in dic:
        dic[i] = dic[i] + 1
    else:
        dic[i] = 1

for k,v in dic.items():
    print(k, "occurs", v, "times")