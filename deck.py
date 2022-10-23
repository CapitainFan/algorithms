class Deck:
    ''' this's the special class - deck '''
    def __init__(self, max_size: int) -> None:
        self.__elements = [None] * max_size
        self.__max_size = max_size
        self.__head = 0
        self.__tail = 0
        self.__size = 0

    def _is_empty(self) -> bool:
        return self.__size == 0

    def _is_full(self) -> bool:
        return self.__size == self.__max_size

    def push_back(self, value) -> None:
        if self._is_full():
            raise OverflowError
        self.__elements[self.__tail] = value
        self.__tail = (self.__tail + 1) % self.__max_size
        self.__size += 1

    def push_front(self, value) -> None:
        if self._is_full():
            raise OverflowError
        self.__elements[self.__head - 1] = value
        self.__head = (self.__head - 1) % self.__max_size
        self.__size += 1

    def pop_back(self):
        if self._is_empty():
            raise IndexError
        x = self.__elements[self.__tail - 1]
        self.__elements[self.__tail - 1] = None
        self.__tail = (self.__tail - 1) % self.__max_size
        self.__size -= 1
        return x

    def pop_front(self):
        if self._is_empty():
            raise IndexError
        x = self.__elements[self.__head]
        self.__elements[self.__head] = None
        self.__head = (self.__head + 1) % self.__max_size
        self.__size -= 1
        return x


def main() -> None:
    count_command = int(input())
    queue_size = int(input())
    queue = Deck(queue_size)

    for _ in range(count_command):
        command = input()
        operation, *value = command.split()
        try:
            function = getattr(queue, operation)
            result = function(int(*value)) if value else function()
            if result is not None:
                print(result)
        except (IndexError, OverflowError):
            print('error')


if __name__ == '__main__':
    main()
