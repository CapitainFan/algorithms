def calculations(strit_len: int, houses_list: list) -> int:
    ''' this function will get list
        of numbers and return a list
        of the same length where instead
        of numbers, the number of elements
        from the number to the nearest
        zero is indicated'''
    function_result = [0] * strit_len
    index_last_0 = -strit_len

    for i in range(strit_len):
        if houses_list[i]:
            function_result[i] = i - index_last_0
        else:
            index_last_0 = i

    index_last_0 = strit_len*2

    for i in reversed(range(strit_len)):
        if houses_list[i]:
            function_result[i] = min(index_last_0-i, function_result[i])
        else:
            index_last_0 = i

    return function_result


def main() -> None:
    house_count = int(input())
    house_numbers = [int(number) for number in input().split()]
    result = calculations(house_count, house_numbers)
    print(*result)


if __name__ == "__main__":
    main()
