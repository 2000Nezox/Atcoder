while True:
    H,W = map(int,input().split())
    if H == W == 0:
        break
    else:
        print("#"*W)
        for i in range(H-2):
            print("#"+"."*(W-2)+"#")
        print("#"*W)
    print('')