#버블정렬
#시간복잡도: O(N^2)
#차례로 인접한 두 개의 원소를 비교하여 자리를 교환하는 정렬 알고리

def BubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:   #내림차순은 부호를 반대로 사용
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print("step",i,arr)   

arr = list(map(int,input().split()))
BubbleSort(arr)
