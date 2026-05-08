from src.my_stack import MyStack


def is_valid_parentheses(string: str) -> bool:
    pilha = MyStack()

    for caractere in string:
        if caractere == '(' or caractere == '[' or caractere == '{':
            pilha.push(caractere)

        else:
            if pilha.is_empty():
                return False

            topo = pilha.pop()

            if caractere == ')' and topo != '(':
                return False
            if caractere == ']' and topo != '[':
                return False
            if caractere == '}' and topo != '{':
                return False

    return pilha.is_empty()
