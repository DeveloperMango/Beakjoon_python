#2941번   : 크로아티아알파벳
#참고     : https://www.acmicpc.net/problem/2941

alpha = ['c=','c-','dz=','d-','lj','nj','s=','z=']

sentence = input()
cnt = 0
i=0

while i < len(sentence):
    if sentence[i:i+3] in alpha:
        i+=3
    elif sentence[i:i+2] in alpha :
        i+=2
    else:
        i+=1
        
    cnt+=1
        
print(cnt)
