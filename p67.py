class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        np1 = len(a) - 1
        np2 = len(b) - 1
        ans = ''
        isJ = False

        while np1 >= 0 and np2 >= 0:
            if isJ :
                if a[np1] == '1' :
                    isJ = True
                    if b[np2] == '1':
                        ans += '1'
                    else:
                        ans += '0'
                else:
                    if b[np2] == '1':
                        isJ = True
                        ans += '0'
                    else:
                        isJ = False 
                        ans += '1'
            else:
                if a[np1] == '1' :
                    if b[np2] == '1':
                        isJ =True
                        ans += '0'
                    else:
                        isJ = False
                        ans += '1'
                else:
                    isJ = False
                    if b[np2] == '1':
                        ans += '1'
                    else:
                        ans += '0'
            np1 -= 1
            np2 -= 1
        while np1 >= 0:
            if isJ :
                if a[np1] == '1':
                    isJ = True
                    ans += '0'
                else:
                    isJ = False
                    ans += '1'
            else:   
                isJ = False
                ans += a[np1]
            np1 -= 1
        while np2 >= 0:
            if isJ :
                if b[np2] == '1':
                    isJ = True
                    ans += '0'
                else:
                    isJ = False
                    ans += '1'
            else:   
                isJ = False
                ans += b[np2]
            np2 -= 1
        if isJ:
            ans += '1'
        anslist = list(ans) 
        anslist.reverse()
        fans = ''.join(anslist)
        return fans

print(Solution().addBinary('1010','1011'))
print(Solution().addBinary('11','1'))
