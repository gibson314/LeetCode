class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        resultString = s[::-1]


        return resultString


if __name__ == '__main__':
    sol = Solution()
    print(sol.reverseString("helloworld"))