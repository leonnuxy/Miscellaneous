# Write a program that:
    # Input: num = [1,2,0,0], k = 34
    # Output: [1,2,3,4]
    # Explanation: 1200 + 34 = 1234

class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        num = [str(i) for i in num]
        num = ''.join(num)
        num = int(num)
        num += k
        num = str(num)
        num = [int(i) for i in num]
        return num