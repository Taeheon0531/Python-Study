N , M = map(int, input().split())
basket = []
for n in range(N):
    basket.append(n+1)
for m in range(M):
    i, j = map(int, input().split())
    x = basket[i-1]
    y = basket[j-1]
    basket[i-1] = y
    basket[j-1] = x
for n in range(N):
    print(basket[n], end=" ")

#Better code
N , M = map(int, input().split())
basket = [str(i+1) for i in range(N)]
for exchange in range(M):
    i, j = map(int, input(.split(' ')))
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]
print(' '.join(basket))