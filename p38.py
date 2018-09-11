class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        prestr = self.countAndSay(n-1)
        np = prestr[0]
        cou = 1
        ans = ''
        if len(prestr) > 1:
            for si in prestr[1:]:
                if si == np:
                    cou += 1
                else: # si != np
                    ans += str(cou)
                    ans += str(np)
                    np = si
                    cou = 1
            if prestr[-1] == np:
                ans += str(cou)
                ans += str(np)
        else:
            ans = '11'
        return ans

for i in range(1,10):
    print(Solution().countAndSay(i))
               



