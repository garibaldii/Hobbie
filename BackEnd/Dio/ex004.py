T = int(input())
if (T >= 1) and (T <= 10000):
    for i in range(1,T+1):
        N, K = map(int, input().split())
        if (K >= 1) and (N <= 10000):
            X = int((N / K) + (N % K))
            print(X)
            