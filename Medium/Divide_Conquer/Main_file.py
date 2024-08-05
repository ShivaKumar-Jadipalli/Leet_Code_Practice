class Divide:
    def merge(self,given_1,given_2):
        answer = []
        while True:
            if given_1[-1]>given_2[-1]: # [2,5],[-1,3]
                popped_value = given_1.pop()
            else:
                popped_value = given_2.pop()
            answer.append(popped_value)
            if len(given_1)==0 or len(given_2)==0:
                answer.extend(given_2[::-1])
                answer.extend(given_1[::-1])
                return answer[::-1]
    def main_code(self,given):
        if len(given)<2:
            return given
        middle = len(given)//2 
        first_half = self.main_code(given[:middle])
        second_half = self.main_code(given[middle:])
        return self.merge(first_half, second_half)  
data = [*range(30,1,-1)]
print(Divide().main_code(data))