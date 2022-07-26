
from termios import NL1


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
       
        # defining a blank res variable
        res = ""
         
        # initializing ptr to head
        ptr = self
         
       # traversing and adding it to res
        while ptr:
            res += str(ptr.val) + ", "
            ptr = ptr.next
 
       # removing trailing commas
        res = res.strip(", ")
         
        # chen checking if
        # anything is present in res or not
        if len(res):
            return "[" + res + "]"
        else:
            return "[]"


class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        p1_head = head
        p1_end = head
        
        for i in range(1, left - 1):
            p1_end = p1_end.next
          
        p2_head = p1_end.next
        p1_end.next = None
            
        p2_end = p2_head    
        
        for i in range (left, right):
            p2_end = p2_end.next
            
        p3_head = p2_end.next
        p2_end.next = None
        
        p1_end.next = self.reverse(p2_head)
        
        p2_head.next = p3_head
        
        return p1_head
        
        
    def reverse(self, head):
  
        if head is None or head.next is None:
            return head

        rest = self.reverse(head.next)
  
        head.next.next = head
        head.next = None
  
        return rest

if __name__ == "__main__":

    n5 = ListNode(6)
    n4 = ListNode(5, n5)
    n3 = ListNode(4, n4)
    n2 = ListNode(3, n3)
    n1 = ListNode(2, n2)
    head = ListNode(1, n1)

    solution = Solution()
    print(solution.reverseBetween(head, 3, 5))