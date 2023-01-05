from data_structures.stack import Stack


def multi_bracket_validation(string):
    stack = Stack()
    open_b = ['(', '[', '{']
    closed_b = [')', ']', '}']
    for char in string:
        if char in open_b:
            stack.push(char)
        elif char in closed_b:
            if stack.is_empty():
                return False
            else:
                popped = stack.pop()
                if open_b.index(popped) == closed_b.index(char):
                    pass
                else:
                    return False
    else:
        pass

    if not stack.is_empty():
        return False
    return True

