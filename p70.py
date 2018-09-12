class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n == 1:
            # return 1
        # if n == 2:
            # return 2
        # return self.climbStairs(n - 1 ) + self.climbStairs(n - 2)
        f1 , f2 = 1 , 2
        for i in range(2,n+1):
            f1 , f2 = f2 , f1 + f2
        return f1

