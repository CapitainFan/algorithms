class Stack:
    ''' this's the special class - stack'''
    def __init__(self) -> None:
        self.__values = []

    def push(self, value: int) -> None:
        self.__values.append(value)

    def pop(self) -> int:
        result = self.__values.pop()
        return result


def calculations(tokens: list) -> int:
    ''' this function will get calculations
        on poland notations and return solution '''
    stack = Stack()

    OPERATIONS = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x // y,
    }

    for token in tokens:
        try:
            stack.push(int(token))
        except ValueError:
            second_operand = stack.pop()
            first_operand = stack.pop()
            result = OPERATIONS[token](first_operand, second_operand)
            stack.push(int(result))

    return stack.pop()


def main() -> None:
    tokens = input().split()
    print(calculations(tokens))


if __name__ == '__main__':
    main()
