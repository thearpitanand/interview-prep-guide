class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        curr = self
        result = []
        while curr:
            result.append(str(curr.val))
            curr = curr.next
        print(result)
        return " -> ".join(result) + " -> None"

    def __eq__(self, other):
        curr_self, curr_other = self, other

        while curr_self and curr_other:
            if curr_self.val != curr_other.val:
                return False
            curr_self = curr_self.next
            curr_other = curr_other.next

        return curr_self is None and curr_other is None

    def __len__(self):
        curr = self
        count = 0
        while curr is not None:
            count += 1
            curr = curr.next
        return count


ll_nodes_1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
ll_nodes_1_duplicate = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
ll_nodes_2 = ListNode(6, ListNode(7, ListNode(8, ListNode(9, ListNode(10)))))

print(ll_nodes_1 == ll_nodes_1_duplicate)
print(ll_nodes_1 == ll_nodes_2)
print(len(ll_nodes_1))
print(len(ll_nodes_2))
