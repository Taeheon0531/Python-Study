N , M = map(int, input().split())
basket = [0] * N

for l in range(M):
    i, j, k = map(int, input().split())
    for n in range(i-1, j):
        basket[n] = k

for i in range(N):
    print(basket[i], end=" ")

# end=" "는 현재 속한 출력물을 그 다음 출력값과 이어지게 한다