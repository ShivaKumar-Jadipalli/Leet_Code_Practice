
from functools import lru_cache  # Python 3 caching decorator for optimization

class Solution:
    def numberOfWays(self, start_pos: int, end_pos: int, num_steps: int) -> int:
        # Define the modulo constant to avoid large numbers
        MOD = 10 ** 9 + 7
      
        @lru_cache(maxsize=None)  # Cache the results of the function calls
        def dfs(current_pos: int, steps_remaining: int) -> int:
            # We can't reach the target if we are too far or steps are negative
            if current_pos > steps_remaining or steps_remaining < 0:
                return 0
            # If no steps remaining, check if we are at the start
            if steps_remaining == 0:
                return 1 if current_pos == 0 else 0
            # Calculate the number of ways by going one step forward or backward
            # Use modulo operation to keep numbers in a reasonable range
            return (dfs(current_pos + 1, steps_remaining - 1) + 
                    dfs(abs(current_pos - 1), steps_remaining - 1)) % MOD

        # The absolute difference gives the minimum number of steps required
        # Call the dfs function with the absolute difference and the number of steps
        return dfs(abs(start_pos - end_pos), num_steps)

# solution_instance = Solution()
# print(solution_instance.numberOfWays(1, 2, 3))  # Example call to the method
