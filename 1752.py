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
            # nums[(i+1)%n] torna a comparação circular, ou seja o último elemento vai poder ser comparado com o primeiro
            # se precisar de referência futura o rian do passado escreveu a equação com exemplo no caderno
            if nums[i] > nums[(i+1)%n]:
                cont += 1
        
        # se a ordem quebrar no máximo uma vez, o aray já está sorted e rotated
        return cont <= 1