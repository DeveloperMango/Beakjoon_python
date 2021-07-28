while True:
    tri = sorted(list(map(int, input().split())))

    if 0 in tri:
        break

    if ((tri[0] ** 2) + (tri[1] ** 2)) == (tri[2] ** 2):
        print("right")
    else:
        print("wrong")
