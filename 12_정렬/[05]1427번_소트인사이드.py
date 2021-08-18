#1427번: 소트인사이드
#https://www.acmicpc.net/problem/1427


arr = list(input())

for i in range(len(arr)):
    tmp = i
    for j in range(i+1,len(arr)):
        if(arr[tmp]<=arr[j]): tmp = j 

    arr[i],arr[tmp] = arr[tmp],arr[i]
    print(arr[i],end="")     
