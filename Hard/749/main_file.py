given_word = input("Enter the word : \n")
required_word = input("Enter Search Word : \n")
answer = 0
for i in given_word:
    if required_word == i :
        answer += 1
print(required_word ,' : ',answer)