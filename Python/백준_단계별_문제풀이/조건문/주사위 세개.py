a,b,c = map(int, input().split())
if a==b==c:
    print(f'{10000+a*1000}')
elif a==b and b!=c:
    print(f'{1000+a*100}')
elif a==c and c!=b:
    print(f'{1000+a*100}')
elif b==c and b!=a:
    print(f'{1000+b*100}')
else:
    print(f'{max(a,b,c)*100}')