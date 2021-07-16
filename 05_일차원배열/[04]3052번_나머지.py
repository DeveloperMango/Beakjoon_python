#3052번_나머지

n_list = [int(input()) for i in range(0,10)]
ck_list = []

for i in n_list:
    ck_list.append(i%42)

my_set = set(ck_list)
new_list = list(my_set)
print(len(new_list))
