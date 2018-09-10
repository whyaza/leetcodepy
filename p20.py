class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for si in s:
            if si == '(' or si == '{' or si == '[':
                stack.append(si)
            elif si == ')' and len(stack)>0 and stack[-1] == '(':
                stack.pop()
            elif si == '}' and len(stack)>0 and stack[-1] == '{':
                stack.pop()
            elif si == ']' and len(stack)>0 and stack[-1] == '[':
                stack.pop()
            else :
                return False
        return True if len(stack) == 0 else False

print(Solution().isValid('{[]}'))
print(Solution().isValid(']('))

