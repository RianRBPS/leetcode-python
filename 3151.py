 
class Solution(object):
    def isArraySpecial(self, nums):
        """
        the loop will run o(n) times, comparing i to i+1 to see if they are both even or odds
        in case there's two numbers that are even or odds next to each other return false
        otherwise returns true
        """
        for i in range(len(nums) - 1):
            if nums[i] % 2 == nums[i + 1] % 2:
                return False
        return True
        