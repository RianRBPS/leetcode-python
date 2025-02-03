class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cont = 0
        n = len(nums)

        # contando quantas vezes a ordem quebra
        for i in range(n):
            if nums[i] > nums[(i+1)%n]:
                cont += 1
        
        # se a ordem quebrar no máximo uma vez, o aray já está sorted e rotated
        return cont <= 1