#1110번: 더하기 사이클
#26부터 시작한다. 2+6 = 8이다. 새로운 수는 68이다. 6+8 = 14이다.
#새로운 수는 84이다. 8+4 = 12이다. 새로운 수는 42이다. 4+2 = 6이다.
#새로운 수는 26이다.


num = input()
cnt = 0

if int(num)<10:
   arr = ['0',num]
else: 
   arr = list(num)
   
while True:
   a = int(arr[0])
   b = int(arr[1])
   
   if a+b<10:
      arr[0] = arr[1]
      arr[1] = a+b
   else:
      arr[0] = arr[1]
      n = list(map(int,str(a+b)))
      arr[1] = n[1]

   if int(arr[0])==0:
      temp = arr[1]
   else:
      temp = ''.join(map(str,arr))

   
   if str(num)==str(temp): #str을 제거하면 FLASE / print(num==temp) =FALSE
      cnt+=1
      break
   else:
      cnt+=1
      
print(cnt)


