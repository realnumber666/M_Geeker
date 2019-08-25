# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if not pHead:
            return None
        # 1. 复制节点
        h = pHead
        while h.next is not None:
            if h is not pHead:
                h = h.next
            node = RandomListNode(h.label)
            node.next = h.next
            h.next = node
            h = node

        # 2. 指向random node
        l = pHead
        r = l.next
        while r.next is not None:
            if l.random is not None:
                r.random = l.random.next
            r = r.next.next
            l = l.next.next
        if l.random is not None:
            r.random = l.random.next

        # 3. 拆分链表
        l = pHead
        r = l.next
        ret = r
        while r.next is not None:
            l.next = l.next.next
            r.next = r.next.next
            l = l.next
            r = r.next
        l.next = None
        r.next = None
        return ret

a = RandomListNode('a')
b = RandomListNode('b')
c = RandomListNode('c')
d = RandomListNode('d')
e = RandomListNode('e')

a.next = b
a.random = c
b.next = c
b.random = e
c.next = d
d.next = e
d.random = b

Solution().Clone(e)