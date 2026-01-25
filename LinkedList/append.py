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