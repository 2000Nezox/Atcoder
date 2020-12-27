import statistics

while True:
    n = int(input())
    if n == 0:
        break
    lst = list(map(int, input().split()))
    print(round(statistics.pstdev(lst), 8))
