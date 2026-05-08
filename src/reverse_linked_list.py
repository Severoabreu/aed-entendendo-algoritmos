from src.my_node import MyNode


def reverse_linked_list(head: MyNode) -> MyNode:
    if not head or not head.next:
        return head

    anterior = None
    atual = head

    while atual:

        proximo = atual.next
        atual.next = anterior

        anterior = atual
        atual = proximo

    return anterior
