#1316번   :그룹단어체커
#참고     :https://www.acmicpc.net/problem/1316
# https://andamiro25.tistory.com/46



cnt = int(input())
res=0

for i in range(cnt):
    str = input()
    for i in range(len(str)):
        
        if i == len(str)-1:
            res+=1
            break
        
        if str.count(str[i])>1:
            if str[i] == str[i+1]:  pass
            elif str[i] in str[i+1:]:   break
        
print(res)
