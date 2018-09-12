# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        np = head.next
        fnp = head
        while np:
            if np.val == fnp.val:
                fnp.next = np.next
            else:
                fnp = fnp.next
            np = np.next 
        return head


if __name__ == '__main__':
    head = ListNode(0)
    nh = head
    ls = []
    for l in ls:
        li = ListNode(l)
        nh.next = li
        nh = nh.next
    
#     np = head
    # while np:
        # print(np.val)
        # np = np.next
    
    gh = Solution().deleteDuplicates(head)
    while gh:
        print(gh.val)
        gh = gh.next
    

