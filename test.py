list1 = [6,56,45,-8,-45,78,44]

print (list1)
for i in range(len(list1)):


    min_val = min(list1[i: ])   #in this line it will chek the min value in the list that is zero with the helo of min method


    min_ind = list1.index(min_val)

    temp = list1[i]
    list1[i] = list1[min_ind]
    list1[min_ind] = temp
    print(list1)
