import math
class Prime:
    def check_prime(self,n):
        for i in range(2,int(math.sqrt(n))+1):
            if n%i == 0:
                return False 
        return True 
    def prime_numbers(self,n):
        results  = []
        count = 2
        while len(results) < n:
            if self.check_prime(count):
                results.append(count)
            count+=1
        print(results)
        return results
    def differences(self,n):
        given_list = self.prime_numbers(n) 
        results = []
        first_number = given_list[0]
        for i in given_list[1:]:
            results.append(i-first_number)
            first_number = i 
        print(results)

Prime().differences(70)