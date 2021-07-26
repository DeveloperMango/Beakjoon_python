#11729번: 하노이탑 이동 순서.py
#https://www.acmicpc.net/problem/11729
#도저히 몰라서 다른사람 코드를 해석함


#옮겨야하는 원판갯수, 출발, 중간, 도착
def hanoi(n, p1, p2, p3):
    if n == 1:
        print(p1, p3)
        return
    
    hanoi(n-1, p1, p3, p2)
    print(p1, p3)
    hanoi(n-1, p2, p1, p3)

num = int(input())
print((2**num)-1)   #하노이수열 공식: 2^n-1
print(hanoi(num,1,2,3))
