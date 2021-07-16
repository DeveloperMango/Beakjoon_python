#8958번: OX퀴즈


cnt = int(input())

for i in range(0,cnt):
    
    score = input()
    ck = 1
    num = 0

    for j in range(0,len(score)):
        if score[j] == "O":
            num += ck
            ck += 1 
        else:
            ck = 1
            
    print(num)
