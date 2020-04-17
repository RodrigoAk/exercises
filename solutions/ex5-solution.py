'''
Given a singly-linked list, reverse the list. This can be done iteratively
or recursively. Can you get both solutions?

Example:
Input: 4 -> 3 -> 2 -> 1 -> 0 -> NULL
Output: 0 -> 1 -> 2 -> 3 -> 4 -> NULL
'''


class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

  # Function to print the list
  def printList(self):
    node = self
    output = ''
    while node != None:
      output += str(node.val)
      output += " "
      node = node.next
    print(output)

  # Iterative Solution
  def reverseIteratively(self, head):
    prev = None
    while(head is not None): # Imagine uma lista: NULL   1 -> 2 -> 3 -> NULL
        next = head.next     # Queremos trocar as setas de sentido apenas
        head.next = prev     # NULL(prev) 1(node) -> 2 (next) -> 3 -> NULL
        prev = head          # NULL(prev) <- 1(node)  2(next) -> 3 -> NULL
        head = next          # NULL <- 1(prev)(node)  2(next) -> 3 -> NULL
    head = prev              # NULL <- 1(prev)  2(node) -> 3(next) -> NULL  (e repetir os passos)

  # Recursive Solution
  def reverseRecursively(self, head, prev = None):
    next = head.next
    head.next = prev
    if(next is None):
        return head
    else:
        return self.reverseRecursively(next, head)

# Test Program
# Initialize the test list:
testHead = ListNode(4)
node1 = ListNode(3)
testHead.next = node1
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(1)
node2.next = node3
testTail = ListNode(0)
node3.next = testTail

print("Initial list: ")
testHead.printList()
# 4 3 2 1 0
# testHead.reverseIteratively(testHead)
testHead.reverseRecursively(testHead)
print("List after reversal: ")
testTail.printList()
# 0 1 2 3 4
