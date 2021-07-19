
str = input().upper()
str_list = list(set(str))
cnt=0
for i in str_list:
    if(cnt<str.count(i)):
        cnt = str.count(i)
        ch = i
    elif(cnt == str.count(i)):
        ch = '?'
print(ch)
