"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        ''' Method 1 :
        We can traverse through the list and keep creating  the deep copy nodes correspondingly. In order to avoid making repeated deep copy nodes, we can maintain a hashmap (node : deep copy node)to check if the the deep copy of that node has been created or not. '''
        
        '''Method 2: (Optimized Method 1):
        1.First pass
        Create a copy of current node and point the next of the pointer to the copied node
        curr.next= new node
        2. Second pass --> create random pointers
        curr.next.random=curr.random.next
        3. Delete the connections and seperate the linked lists
        '''
        #Time Complexity: O(n)
        #Space Complexity: O(1)
        
        #Edge case
        if not head:
            return None
        
        # First Pass: Create a deep copy node and map it to the original node
        curr=head
        
        while curr is not None:
            #Make a copy
            newNode=Node(curr.val)
            newNode.next=curr.next
            curr.next=newNode
            curr=curr.next.next
            
        #Second pass: Create random pointer connection
        curr=head
        while curr is not None:
            if curr.random is not None:
                curr.next.random=curr.random.next
            curr=curr.next.next
            
        #Seperate the lists
        curr=head
        copyCurr=curr.next
        copyhead=copyCurr
        while curr is not None:
            curr.next=copyCurr.next
            if copyCurr.next is not None:
                copyCurr.next=copyCurr.next.next
            curr=curr.next
            copyCurr=copyCurr.next
        return copyhead
            
        
        
