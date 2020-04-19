class ListNode(object):
    def __init__(self,elem):
        self.elem = elem
        self.next = None

    def __str__(self):
        s = ""
        while self:
            s += str(self.elem) + " -> "
            self = self.next
        return s + "None"


def mergeTwoSortedLists(listNode1, listNode2):
    """
    21. 合并两个有序链表
        将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

        示例：
            输入：1->2->4, 1->3->4
            输出：1->1->2->3->4->4

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
    """
    if not listNode1:
        return listNode2
    if not listNode2:
        return listNode1
    cur  = ListNode(-1)
    head = cur
    while listNode1 and listNode2:
        if listNode1.elem <= listNode2.elem:
            cur.next = listNode1
            listNode1 = listNode1.next
            cur.next.next = listNode2
        else:
            cur.next = listNode2
            listNode2 = listNode2.next
            cur.next.next = listNode1
        cur = cur.next
    return head.next


if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    print(mergeTwoSortedLists(l1,l2))