test = [1, 3, 7, 9, 2,9, 4]
test = [2,4,5,2,5,5,2,1,1,3]
max_value = max(test)
max_indices = [i for i, x in enumerate(test) if x == max_value]
if len(max_indices)>1:
    test_len = len(test)//2
    results = []
    for i in max_indices:
        results.append(abs(test_len - i))
    print('min in results ',min(results))
    print('results list ',results)
    answer = min(results)
    answer = results.index(answer)
    answer = max_indices[answer]
    print(answer)