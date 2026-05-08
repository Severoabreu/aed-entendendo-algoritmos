from src.my_node import MyNode


def has_cycle(head: MyNode) -> bool:
    if not head or not head.next:
        return False
    
    tartaruga = head
    lebre = head

    while lebre and lebre.next:
        tartaruga = tartaruga.next
        lebre = lebre.next.next

        if tartaruga == lebre:
            return True
        
    return False