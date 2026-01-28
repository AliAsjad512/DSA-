class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

        def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

        def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


        # ========== 1. Length of Linked List ==========
def length_of_linked_list(head):
    """
    Returns the length (number of nodes) of the linked list.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    return count


def search_in_linked_list(head, target):
    """
    Search for a target value in the linked list.
    Returns True if found, False otherwise.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    current = head
    while current:
        if current.data == target:
            return True
        current = current.next
    return False

def delete_head(head):
    """
    Delete the head node of the linked list.
    Returns the new head of the list.
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    if not head:
        return None
    new_head = head.next
    # Optional: Free memory of old head (not necessary in Python)
    return new_head


def delete_at_position(head, position):
    """
    Delete node at given position (0-indexed).
    Returns the head of the modified list.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not head:
        return None
    
    # If deleting the head
    if position == 0:
        return head.next
    
    current = head
    prev = None
    count = 0

    while current and count < position:
        prev = current
        current = current.next
        count += 1
    
    # If position is valid and node exists
    if current:
        prev.next = current.next
    return head



def is_linked_list_sorted(head, ascending=True):
    """
    Check if the linked list is sorted.
    ascending=True checks for ascending order, False for descending.
    Returns True if sorted, False otherwise.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not head or not head.next:
        return True
    
    current = head
    while current.next:
        if ascending:
            if current.data > current.next.data:
                return False
        else:
            if current.data < current.next.data:
                return False
        current = current.next
    
    return 

def remove_duplicates_sorted(head):
    """
    Remove duplicates from a sorted linked list.
    Returns the head of the modified list.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not head or not head.next:
        return head
    
    current = head
    while current and current.next:
        # If current node's value equals next node's value
        if current.data == current.next.data:
            # Skip the next node
            current.next = current.next.next
        else:
            # Move to next node
            current = current.next
    
    return head


def are_identical_lists(head1, head2):
    """
    Check if two linked lists are identical.
    Returns True if identical, False otherwise.
    Time Complexity: O(min(n, m))
    Space Complexity: O(1)
    """
    current1 = head1
    current2 = head2
    
    while current1 and current2:
        if current1.data != current2.data:
            return False
        current1 = current1.next
        current2 = current2.next
    
    # If both lists are exhausted, they're identical
    # If one still has nodes, they're not identical
    return current1 == None and current2 == None
def test_all_functions():
    print("Testing Linked List Functions")
    print("=" * 50)
    
    # Create test linked lists
    list1 = LinkedList()
    for value in [1, 2, 3, 4, 5]:
        list1.append(value)
    
    list2 = LinkedList()
    for value in [1, 2, 2, 3, 4, 4, 4, 5]:
        list2.append(value)
    
    list3 = LinkedList()
    for value in [1, 2, 3, 4, 5]:
        list3.append(value)
    
    list_sorted_asc = LinkedList()
    for value in [1, 2, 3, 4, 5]:
        list_sorted_asc.append(value)
    
    list_sorted_desc = LinkedList()
    for value in [5, 4, 3, 2, 1]:
        list_sorted_desc.append(value)
    
    list_unsorted = LinkedList()
    for value in [1, 3, 2, 5, 4]:
        list_unsorted.append(value)
    
    # Test 1: Length of Linked List
    print("1. Length of Linked List:")
    print(f"   List1: {length_of_linked_list(list1.head)}")
    print(f"   List2: {length_of_linked_list(list2.head)}")
    print(f"   Empty list: {length_of_linked_list(None)}")
    print()
    
    # Test 2: Search In Linked List
    print("2. Search In Linked List:")
    print(f"   Search 3 in List1: {search_in_linked_list(list1.head, 3)}")
    print(f"   Search 10 in List1: {search_in_linked_list(list1.head, 10)}")
    print()
    
    # Test 3: Delete Head of Linked List
    print("3. Delete Head of Linked List:")
    print("   Original List1:", end=" ")
    list1.print_list()
    
    new_head = delete_head(list1.head)
    temp_list = LinkedList()
    temp_list.head = new_head
    print("   After deleting head:", end=" ")
    temp_list.print_list()
    print()

    print("4. Linked List Delete at Position:")
    # Reset list1 for testing
    list1 = LinkedList()
    for value in [1, 2, 3, 4, 5]:
        list1.append(value)
    
    print("   Original list:", end=" ")
    list1.print_list()
    
    # Delete at position 2 (0-indexed, so 3rd element)
    list1.head = delete_at_position(list1.head, 2)
    print("   After deleting at position 2:", end=" ")
    list1.print_list()
    print()
    
     print("5. Is Linked List Sorted:")
    print(f"   Ascending sorted list (ascending check): {is_linked_list_sorted(list_sorted_asc.head, ascending=True)}")
    print(f"   Ascending sorted list (descending check): {is_linked_list_sorted(list_sorted_asc.head, ascending=False)}")
    print(f"   Descending sorted list (ascending check): {is_linked_list_sorted(list_sorted_desc.head, ascending=True)}")
    print(f"   Descending sorted list (descending check): {is_linked_list_sorted(list_sorted_desc.head, ascending=False)}")
    print(f"   Unsorted list (ascending check): {is_linked_list_sorted(list_unsorted.head, ascending=True)}")
    print()