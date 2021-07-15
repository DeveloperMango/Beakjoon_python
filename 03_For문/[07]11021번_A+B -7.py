#11021번: A+B -7
num = int(input())

for i in range(num):
    val1, val2 = input().split()
    print("Case #%d: %d"%(i+1, int(val1)+int(val2)))
