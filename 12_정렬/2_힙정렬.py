#힙정렬
#최소 힙: 부모 노드의 값이 자식 노드의 값보다 작거나 같은 완전이진트리
#최대 힙: 부모 노드의 값이 자식 노드의 값보다 크거나 같은 완전이진트리
#최대 힙 트리나 최소 힙트리를 구성하여 정렬하는 알고리즘

#시간복잡도: O(N*logN)
#최소힙은 부호를 반대로 사용

def heapify(arr, index, heapSize):      #최대힙
        print("step: ",arr)
        largest = index
        l_idx = 2*index+1   #left
        r_idx = 2*index+2   #right

        if l_idx < heapSize and arr[l_idx]>arr[largest]:
            largest = l_idx
        if r_idx < heapSize and arr[r_idx]>arr[largest]:
            largest = r_idx

        if largest != index:
            arr[largest], arr[index] = arr[index],arr[largest]
            heapify(arr, largest, heapSize)

def heap_sort(arr):
    # 최초 힙
    # 트리의 절반부터 거꾸로 올라가며 heapify를 하는것이 효율적
    for i in range(len(arr)//2-1, -1, -1):
      heapify(arr,i,len(arr))

      
    # 한번 구성된 힙을 정렬.
    # 가장 큰 값(루트) 를 가장 끝 값으로 이동한 후 힙 생성.
    for i in range(len(arr)-1,0,-1):
            arr[0], arr[i] = arr[i],arr[0]
            heapify(arr,0,i)
        
    return arr
    

arr = list(map(int,input().split()))
print(heap_sort(arr))

