x, y, w, h = map(int, input().split())

#x-0, y-0
distance = [x, y, w-x, h-y]
print(min(distance))
