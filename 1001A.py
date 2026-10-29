k = int(input())
for _ in range(k): 
    posible = False
    n ,k= map(int,input().split())
    a = list(map(int, input().split()))
    a1 = [abs(a[0])]
    for i in range(n-1):
        a1.append(a[i+1]-a[i])
    a1.append(2*(k-a[-1]))
    print(max(a1))
    