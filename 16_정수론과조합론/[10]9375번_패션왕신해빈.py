#9375번: 패션왕 신해빈
#https://www.acmicpc.net/problem/9375



import sys
cnt = int(sys.stdin.readline())

for _ in range(cnt):
    num = int(sys.stdin.readline())
    arr = {}

    for i in range(num):
        l,r = sys.stdin.readline().split()
        if r in arr.keys():
            arr[r].append(l)
        else:
            arr[r]=[l,""]
    ans = 1

    for key in arr.keys():
        ans *= len(arr[key])

    print(ans-1)

