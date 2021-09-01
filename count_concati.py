st = "aabbbbeeeeffggg"
new_st = ""
count = 0
toCheck = st[0]

for j in range(0, len(st)):

    if toCheck == st[j]:
        count = count + 1

    else:
        if count > 1:
            new_st = new_st + toCheck + str(count) 

        else:
            new_st = new_st + toCheck

        toCheck = st[j]
        count = 1

if count > 1:
    new_st = new_st +toCheck+str(count)
else:
    new_st = new_st +toCheck

print(new_st)

