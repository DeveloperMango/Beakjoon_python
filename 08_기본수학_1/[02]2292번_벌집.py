#2292번: 벌집

num =int(input())

cnt = 1
res = 1

while True:
    if res >= num:
        break
    else:
        tmp = 6*cnt
        cnt+=1
        res += tmp  

print(cnt)
  


        
