from src.my_node import MyNode


def kth_to_last(head: MyNode, k: int) -> int:
    if not head or k <= 0:
        return -1

    ponteiro_frente = head
    ponteiro_atras = head

    for _ in range(k):
        if not ponteiro_frente:
            return -1
        ponteiro_frente = ponteiro_frente.next

    while ponteiro_frente:
        ponteiro_frente = ponteiro_frente.next
        ponteiro_atras = ponteiro_atras.next

    return ponteiro_atras.value
