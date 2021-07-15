#2439번: 별찍기-2
num = int(input())

for i in range(num-1,-1,-1):
    print(" "*i,end='')           
    for j in range(num):
        if i<=j:
            print("*",end='')
    print()
