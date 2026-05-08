from src.my_node import MyNode


def remove_duplicates(head: MyNode) -> MyNode:
    if not head:
        return head

    atual = head

    while atual:
        corredor = atual

        while corredor.next:
            if corredor.next.value == atual.value:
                corredor.next = corredor.next.next

            else:
                corredor = corredor.next

        atual = atual.next

    return head
