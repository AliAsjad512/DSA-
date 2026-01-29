# Node class for Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None
    
    # Utility function to add a node at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    # Utility function to print the linked list
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

        def insert_at_end(head, data):
    """
    Insert a node at the end of the linked list.
    Returns the head of the modified list.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    new_node = Node(data)
    
    # If list is empty
    if not head:
        return new_node
    
    # Traverse to the last node
    current = head
    while current.next:
        current = current.next
    
    # Insert at the end
    current.next = new_node
    # return head()



def insert_in_middle(head, data):
    """
    Insert a node in the middle of the linked list.
    If length is even, insert after the first middle.
    Returns the head of the modified list.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    new_node = Node(data)
    
    # If list is empty
    if not head:
        return new_node
    
    # Find the length
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    
    # Find middle position
    middle_pos = length // 2
    
    # Traverse to the node before middle position
    current = head
    for _ in range(middle_pos - 1):
        current = current.next
    
    # Insert after current node
    new_node.next = current.next
    current.next = new_node
    
    return head

def insert_at_position(head, data, position):
    """
    Insert a node at a specific position (1-indexed).
    Returns the head of the modified list.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    new_node = Node(data)
    
    # If inserting at position 1 (head)
    if position == 1:
        new_node.next = head
        return new_node
    
    # Traverse to the node before the position
    current = head
    for _ in range(position - 2):
        if not current:
            # Position is beyond the list length
            # Append at the end
            return insert_at_end(head, data)
        current = current.next
    
    # Insert at the position
    if current:
        new_node.next = current.next
        current.next = new_node
    
    return head


def insert_in_sorted_list(head, data):
    """
    Insert a node in a sorted linked list while maintaining the sorted order.
    Returns the head of the modified list.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    new_node = Node(data)
    
    # If list is empty or new node should be the new head
    if not head or head.data >= data:
        new_node.next = head
        return new_node
    
    # Find the correct position
    current = head
    while current.next and current.next.data < data:
        current = current.next
    
    # Insert the new node
    new_node.next = current.next
    current.next = new_node
    
    return head


# ========== 5. Delete Tail of Linked List ==========
def delete_tail(head):
    """
    Delete the last node (tail) of the linked list.
    Returns the head of the modified list.
    Time Complexity: O(n)
    Space Complexity: O(1)
    "