C = int(input())

for i in range(C):
    nums = list(map(int, input().split()))
    avg = sum(nums[1:])/nums[0]
    cnt = 0
    for score in nums[1:]:
        if score > avg:
            cnt += 1
    rate = cnt/nums[0] * 100
    print(f'{rate:.3f}%')

#정신 못차리고 푼 내용