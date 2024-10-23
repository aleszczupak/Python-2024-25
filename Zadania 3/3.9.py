seq_list = [[],[4],(1,2),[3,4],(5,6,7)]

# pętla
sum_list1 = []
for i in seq_list:
    sum_list1.append(sum(i))
print(sum_list1)
print()

# list comprehension
sum_list2 = [sum(i) for i in seq_list]
print(sum_list2)
print()

# map
sum_list3 = list(map(sum, seq_list))
print(sum_list3)
