#10871번: X보다 작은 수

A,B = map(int,input().split())

num_arr = list(map(int,input().split()))

for i in range(A):
    if num_arr[i] <B:
        print(num_arr[i],end=' ')
