#카운팅정렬

#시간복잡도 O(N)
#각자의 숫자가 몇번째로 등장하는지 세어서 정렬
#비교를 하지 않고 정렬하는 특징을 가지고 있음
#max가 커지면 비효율적이다.
#내림차순은 Reverse 한다.

#counting sort 구현
def counting_sort(arr, max):
 
    cnt_arr = [0]*(max+1)
 
    for i in arr:
        cnt_arr[i] += 1
 
    for i in range(max):
        cnt_arr[i+1] += cnt_arr[i]
 
    output_arr = [-1]*len(arr)
  
    for i in arr:
        output_arr[cnt_arr[i]-1] = i
        cnt_arr[i] -= 1
    return output_arr


arr = list(map(int,input().split()))
print(counting_sort(arr,max(arr)))
