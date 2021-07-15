#11022번: A+B -8
num = int(input())

for i in range(num):
    val1, val2=map(int,input().split())
    print("Case #%d: %d + %d = %d"%(i+1,val1,val2,val1+val2))
