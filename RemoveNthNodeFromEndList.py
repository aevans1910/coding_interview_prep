# Leetcode code

# Given a linked list, remove the n-th node from the end of list
# and return its head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time complexity: O(2n) as the code needs to go through the linked list twice
# Space complexity: O(n) as the code creates a list to append n nodes to it      
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        self.tail = None
        
        return_list = [] #O(n) space complexity (n items take n amount of space)
        node = head
        previous_node = None
        node_count = 0
        
        while node != None: #O(n) time to go through n nodes
            node_count += 1
            previous_node = node
            node = node.next
            
        nth_node = node_count - (n)
        
        node = head
        node_count = 0
        
        while node != None: #O(n) time to go through n nodes
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