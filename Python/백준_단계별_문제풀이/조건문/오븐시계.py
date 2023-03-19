H, M = input().split()
addtime = int(input())

H = int(H)
M = int(M)

addhour = addtime // 60
addmin = addtime % 60

if M + addmin >= 60:
    addhour += 1
    M = M + addmin - 60
else:
    M = M + addmin

if H + addhour >= 24:
    H = H + addhour - 24
else:
    H = H + addhour

print(f'{H} {M}')