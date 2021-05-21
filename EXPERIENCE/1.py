n = int(input())
for i in range(n):
    T, m, k = map(int,input().split())
    data = list(map(int.input().split()))
    for j in cost_list:
        for k in cost_list:
        MaxVal = 1000000
        MinVal = data[j] * m
        if MinVal < MaxVal:
            MinVal = 