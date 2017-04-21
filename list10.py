max1 = [
         [1, 3],
         [2, 4]
       ]
max2 = [
         [5, 2],
         [1, 0]
       ]
max_sum = []
for index1 in range(len(max1)):
    max_inner = []
    for index2 in range(len(max1[index1])):
        max_inner.append(max1[index1][index2] + max2[index1][index2])

    max_sum.append(max_inner)

for inner_list in max_sum:
    for inner_num in inner_list:
        print(inner_num, end=" ")

    print("")
[[1,3],[2, 4]]
[]
