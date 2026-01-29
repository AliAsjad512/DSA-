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
    
 if not head or not head.next:
        return None
    
    # Traverse to the second last node
    current = head
    while current.next and current.next.next:
        current = current.next
    
    # Remove the last node
    current.next = None
    
    return head
def join_linked_lists(head1, head2):
    """
    Join two linked lists by connecting the tail of first to head of second.
    Returns the head of the joined list.
    Time Complexity: O(n) where n is length of first list
    Space Complexity: O(1)
    """
    # If first list is empty
    if not head1:
        return head2
    
    # If second list is empty
    if not head2:
        return head1
    
    # Find the tail of first list
    current = head1
    while current.next:
        current = current.next
    
    # Connect tail of first to head of second
    current.next = head2
    
    return head1


# ========== 7. Reverse a linked list ==========
def reverse_linked_list(head):
    prev = None
    current = head
    
    while current:
        # Store the next node
        next_node = current.next
        
        # Reverse the link
        current.next = prev
        
        # Move pointers forward
        prev = current
        current = next_node
    
    # prev is the new head
    return prev

def advanced_testing():
    print("\nAdvanced Testing Scenarios")
    print("=" * 60)
    
    # Test edge cases for each function
    
    print("1. Edge Cases - Empty List Operations:")
    empty_head = None
    
    # Insert at end of empty list
    empty_head = insert_at_end(empty_head, 100)
    temp = LinkedList()
    temp.head = empty_head
    print("   Insert 100 at end of empty list:", end=" ")
    temp.print_list()
    
    # Insert in middle of single element list
    single_list = LinkedList()
    single_list.append(50)
    single_list.head = insert_in_middle(single_list.head, 25)
    print("   Insert 25 in middle of [50]:", end=" ")
    single_list.print_list()
    
    print("\n2. Edge Cases - Boundary Positions:")
    bound_list = LinkedList()
    bound_list.append(1)
    bound_list.append(2)
    
    # Insert at position 0 (should handle as position 1)
    bound_list.head = insert_at_position(bound_list.head, 0, 1)
    print("   After inserting 0 at position 1:", end=" ")
    bound_list.print_list()
    
    # Insert at position beyond length
    bound_list.head = insert_at_position(bound_list.head, 99, 10)
    print("   After inserting 99 at position 10 (beyond length):", end=" ")
    bound_list.print_list()
    
    print("\n3. Edge Cases - Single Element Lists:")
    single = LinkedList()
    single.append(42)
    
    print("   Single element list:", end=" ")
    single.print_list()
    
    # Delete tail of single element list
    single.head = delete_tail(single.head)
    print("   After deleting tail:", end=" ")
    single.print_list()
    
    # Reverse single element list
    single.append(42)
    single.head = reverse_linked_list(single.head)
    print("   After reversing single element:", end=" ")
    single.print_list()


if __name__ == "__main__":
    test_all_functions()
    advanced_testing()
    
    print("\n" + "=" * 60)
    print("All operations tested successfully!")