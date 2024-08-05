given_word = input("Enter a word : \n ")
for i in set(given_word):
    answer = 0
    for j in given_word:
        if j==i:
            answer += 1
    print(i , " :   ", answer)