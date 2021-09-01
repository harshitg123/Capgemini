st = input()

if len(st) > 2:
    
    first_let = st[0]
    last_let = st[-1]

    print(last_let+ st[1:-1] +first_let)

else:
   print(st)