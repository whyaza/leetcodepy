class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        a = []
        if x < 0:
            return False
        while x != 0:
            a.append(x % 10)
            x = x // 10
        return True if a == a[::-1] else False

print(Solution().isPalindrome(121))
print(Solution().isPalindrome(-121))
print(Solution().isPalindrome(10))
