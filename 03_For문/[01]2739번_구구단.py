#2739번: 구구단

num = int(input())
print("\n".join(["%d * %d = %d"%(num,i,num*i) for i in range(1,10)]))


#for i in range(1,10):
#    print(num,"*",i,"=",num*i)



