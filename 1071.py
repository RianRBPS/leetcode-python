class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        # como as duas strings são compostas de concatenações de um mesmo padrão, então 
        if str1 + str2 != str2 + str1:
            return ""
        # ABCABC + ABC = ABC + ABCABC
        # LEET + CODE =! CODE + LEET

        # o tamanho do maior divisor comum é o MDC dos tamanhos das strings

        # função p/ calcular o MDC 
        def mdc(a, b):
            while b:                # enquanto b for maior que zero
                a, b = b, a % b     # atualiza a para b, e atualiza b para a % b (resto da divisão)
            return a                # quando b se torna 0, o valor de a é o MDC

        mdc_length = mdc(len(str1), len(str2))
        # s1 = ABABAB s2 = ABAB
        # padrão = AB
        # MDC(6, 4) = 2

        # retorna o prefixo de str1 com comprimento igual ao MDC encontrado
        return str1[:mdc_length]
        # s1 = ABABAB
        # retorna AB, já que o comprimeto do MDC é 2, que também é o tamanho do padrão AB