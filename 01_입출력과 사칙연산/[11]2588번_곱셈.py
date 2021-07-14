#2588번: 곱셈

a,b = [input() for i in range(0,2)]

for i in range(3,0,-1):
    print(int(a)*int(b[i-1]))
    
print(int(a)*int(b))
