test = [3,3,5,34,35,2,3,5,2,9,29,9,38,37,8]

for i in range(len(test)):
    for j in range(1,len(test)):
        if test[j-1]>test[j]:
            temp = test[j]
            test[j] = test[j-1]
            test[j-1] = temp
print(test)


