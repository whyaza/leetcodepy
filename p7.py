class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        strx = str(x)
        if strx == '0':
            return 0
        ans = 0
        while strx[-1] == '0' :
            strx = strx[0:len(strx)-1]
        ans = int(strx[::-1]) if strx[0] != '-' else int('-'+strx[len(strx):0:-1])
        ans = ans if ( -pow(2,31) ) <= ans <= (pow(2,31) - 1) else 0 
        return ans

print(Solution().reverse(123))
print(Solution().reverse(-123))
print(Solution().reverse(1200))
print(Solution().reverse(120))
print(Solution().reverse(1534236469))

