T = int(input())
for n in range(T):
    R, S = map(str, input().split())
    R = int(R)
    word = ''
    for i in range(len(S)):
        word += S[i]*R
    print(word)