test = input('Enter list like this 1,2,3 : \n')
test = [int(i) for i in test.split(',')] 
for i in range(len(test)):
    start = 0
    end = 1 
    for j in range(len(test)):
        if end < len(test) and (test[start] > test[end]) :
            temp = test[end]
            test[end] = test[start]
            test[start] = temp 
        start += 1 
        end += 1
print(test)