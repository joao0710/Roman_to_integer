"""
Roman_to _integer python translator
    >>> teste = Solution()
    >>> teste.romanToInt('C')
    100
    >>> teste.romanToInt('MCMXCIII')
    1993
    >>> teste.romanToInt('MCMXCIX')
    1999

"""

class Solution:

    def romanToInt(self, s: str) -> int:
        """
        This functions retuns a integer of a roman number
        :param s: string
        :return:  integer
        """
        s = ' ' + s + ' '
        unidade = 0
        dezena = 0
        centena = 0
        milhar = 0
        for i, v in enumerate(s):
            if v == 'M' and s[i - 1] != 'C':   #milhar
                milhar += 1000

            if v == 'C' and s[i - 1] != 'X':   #centena
                centena += 100
            if v == 'D' and s[i - 1] != 'C':
                centena += 500
            if v == 'D' and s[i - 1] == 'C':
                centena += 300
            if v == 'M' and s[i - 1] == 'C':
                centena += 800

            if v == 'X' and s[i - 1] != 'I':    #dezena
                dezena += 10
            if v == 'L' and s[i - 1] != 'X':
                dezena += 50
            if v == 'L' and s[i - 1] == 'X':
                dezena += 30
            if v == 'C' and s[i - 1] == 'X':
                dezena += 80

            if v == 'I':                        #unidade
                unidade += 1
            if v == 'V' and s[i - 1] != 'I':
                unidade += 5
            if v == 'V' and s[i - 1] == 'I':
                unidade += 3
            if v == 'X' and s[i - 1] == 'I':
                unidade += 8
        return milhar + unidade + dezena + centena


if __name__ == '__main__':
    teste = Solution()
    print(teste.romanToInt('CCC'))
