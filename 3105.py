class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        n = len(nums)
        inc_len = 1 # tamanho do subarray de aumento gradual
        dec_len = 1 # tamanho do subarray de diminuindo
        max_len = 1 # maior tamanho encontrado

        for i in range(1, n):
            if nums[i] > nums[i-1]:
                inc_len += 1
                dec_len = 1 # reseta o tamanho do subarray de diminuindo
            elif nums[i] < nums[i-1]:
                dec_len += 1
                inc_len = 1 # reseta o tamanho do subarray de aumentando
            else:   # valor igual os dois resetam
                inc_len = 1
                dec_len = 1

            max_len = max(max_len, inc_len, dec_len)

        return max_len
