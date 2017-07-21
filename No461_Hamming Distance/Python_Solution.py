# in this problem, we consider that using "Exclusive or" to solve
# EOR(^) means that the same logical symbols -> False, the different logical symbols -> True
# For example:
# a = 60 and b = 13
# a = 0011 1100, b = 0000 1101
# a ^ b = 0011 0001
# bin function in Python: convert int to the binary string
# bin(5) = '0b101'

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x ^ y).count('1')
        
