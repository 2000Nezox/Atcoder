S = input()
lst = {"MON":0,"TUE":1,"WED":2,"THU":3,"FRI":4,"SAT":5,"SUN":6}

ans = lst[S]
if ans == 6:
    print(7)
else:
    print(7-ans-1)
