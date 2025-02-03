class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged = []                          # list to store merged charcters
        length = min(len(word1), len(word2)) # min of both lenghts
        
        for i in range (length):             # loop until the lenght of the smaller word
            merged.append(word1[i])
            merged.append(word2[i])
        
        merged.append(word1[length:])        # append the remaining part of the longer string
        merged.append(word2[length:])

        return "".join(merged)               # convert list to string and return