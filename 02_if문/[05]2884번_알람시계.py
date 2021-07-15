#2884번: 알람시계

h,m = map(int,input().split())

print((h-(m<45))%24,(m-45)%60)
