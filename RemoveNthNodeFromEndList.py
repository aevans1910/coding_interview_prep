# Leetcode code

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        self.tail = None
        
        return_list = []
        node = head
        previous_node = None
        node_count = 0
        
        while node != None:
            node_count += 1
            previous_node = node
            node = node.next
            
        nth_node = node_count - (n)
        
        node = head
        node_count = 0
        
        while node != None:
            if node_count != nth_node:
                return_list.append(node.val)
                node_count += 1
                previous_node = node
                node = node.next
            else:
                if node != head and node != self.tail:
                    previous_node.next = node.next
                    node.next = None
                    break
                if node == head:
                    head = node.next
                    node.next = None
                    break
                if node == self.tail:
                    if previous_node != None:
                        previous_node.next = None
                    self.tail = previous_node
                    break
        return head