# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        now = head
        while True:
            arr.append(now.val)
            if now.next == None:
                break
            now = now.next

        n = len(arr)
        answer = ListNode(0)
        node = answer
        for val in arr[:n//2] + arr[n//2+1:]:
            node.next = ListNode(val)
            node = node.next
        
        return answer.next