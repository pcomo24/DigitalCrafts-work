max1 = [
         [1, 3],
         [2, 4]
       ]
max2 = [
         [5, 2],
         [1, 0]
       ]
max_sum = [[0,0],[0,0]]

max_sum[0][0] = max1[0][0] + max2[0][0]
max_sum[0][1] = max1[0][1] + max2[0][1]
max_sum[1][0] = max1[1][0] + max2[1][0]
max_sum[1][1] = max1[1][1] + max2[1][1]
print(max_sum)
