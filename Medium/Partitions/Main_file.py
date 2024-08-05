class Partition:
    def __init__(self,number):
        self.answer = 2
        self.number = number
        temp = [2]
        temp.extend((self.number-2)*[1])
        self.nodes(temp)
        print(self.answer)
    def nodes(self,given):
        try:
            num_1 , given_2 = given.index(1) , given[:] 
        except:
            return 0 
        big_number = self.number if num_1 == 1 else given[num_1-2]
        first_number,second_number = sum(given[num_1-1:num_1+1]) , sum(given_2[num_1:num_1+2])
        if first_number <= big_number:
            given[num_1-1:num_1+1] = [first_number]
            self.answer += 1
            self.nodes(given)
        if second_number <= big_number and len(given_2) >= num_1+2 :
            given_2[num_1:num_1+2] = [second_number]
            self.answer += 1
            self.nodes(given_2)
Partition(8)