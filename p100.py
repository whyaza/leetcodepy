#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        # if (p == None and q != None) or (q == None and p != None):
            # return False

        # if p and q and q.val == p.val:
            # pass
        # elif p == None and q == None :
            # return True
        # else:
            # return False

        # return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

        if p == None and q == None:
            return True
        elif p == None or q == None or p.val != q.val:
            return False
        
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)


    # def test(self,p):
        # if p:
            # print(p.val)
        # else:
            # return
        # self.test(p.left)
        # self.test(p.right)

if __name__ == '__main__':
    thead1 = TreeNode(1)
    thead2 = TreeNode(1)
    t1 = TreeNode(2)
    t2 = TreeNode(3)
    tt = TreeNode(9)
    thead1.left = t1
    thead1.right = t2
    thead2.left = t1
    thead2.right = t2
    # t1.left = tt
    # t1 = TreeNode(2)
    # thead1.left = t1
    # thead2.right = t1

    
    print(Solution().isSameTree(thead1,thead2))
