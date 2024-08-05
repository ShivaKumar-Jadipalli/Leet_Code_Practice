class Solution:
    def get_symbol(self,word):
        return "+" if word>=0 else "-" 
    def asteroidCollision(self, asteroids) :
        asteroids = asteroids[::-1]
        i,j,answers = 0,1,[]
        while j < len(asteroids) :
            if self.get_symbol(asteroids[i]) == self.get_symbol(asteroids[j]): 
                answers.append(asteroids[i])  
                i += 1
                j += 1
            elif asteroids[i] == -asteroids[j]:  # [3,-3]
                i += 2
                j += 2 
            else: 
                bigger = max(abs(asteroids[i]),abs(asteroids[j]))
                if bigger != answers :
                    answers.append(bigger)
                j+=1 
        return answers
    
print(Solution().asteroidCollision([10,2,-5])) # [10]
print(Solution().asteroidCollision([5,10,-5])) # [5,10]
print(Solution().asteroidCollision([8,-8])) # [ ]
