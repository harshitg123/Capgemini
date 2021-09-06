n = int(input())
arr = [int(i) for i in input().split(" ")]

new_arr = list(set(arr))
rem = 0

for i in range(0, len(new_arr)):

    count = arr.count(new_arr[i])
    
    if count % 2 == 0:
            for j in range(0, count, 2):
                rem = rem + 1
    else:
        for k in range(0, count-1, 2):
            rem = rem + 1
print(rem)