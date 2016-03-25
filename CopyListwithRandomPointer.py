class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        d = {}
        if head == None:
            return None
        else:
            nHead = RandomListNode(head.label)
            n1 = head
            n2 = nHead
            n3 = nHead
            d[head] = nHead
            while(head.next!=None):
                head = head.next
                node = RandomListNode(head.label)
                nHead.next = node
                nHead = node
                d[head] = node
            while(n1!=None):
                if n1.random == None:
                    n2.random == None
                else:
                    n2.random = d[n1.random]
                n1 = n1.next
                n2 = n2.next
            return n3   