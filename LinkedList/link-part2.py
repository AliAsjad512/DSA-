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
    return head