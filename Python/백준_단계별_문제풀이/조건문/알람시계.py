H,M = input().split()
H = int(H)
M = int(M)
if M >= 45:
    print(f'{H} {M-45}')
elif H == 0 and M < 45:
    print(f'23 {60-(45-M)}')
else:
    print(f'{H-1} {60-(45-M)}')