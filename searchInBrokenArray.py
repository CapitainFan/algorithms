# Id = 70833472
def broken_search(numbers: list, target: int) -> int:
    left_index = 0
    right_index = len(numbers) - 1

    while left_index <= right_index:
        midle_index = (left_index + right_index) // 2

        if numbers[midle_index] == target:
            return midle_index

        elif numbers[left_index] <= numbers[midle_index]:
            if numbers[left_index] <= target < numbers[midle_index]:
                right_index = midle_index - 1
            else:
                left_index = midle_index + 1

        else:
            if numbers[midle_index] < target <= numbers[right_index]:
                left_index = midle_index + 1
            else:
                right_index = midle_index - 1

    return -1


if __name__ == '__main__':
    array_length = int(input())
    target = int(input())
    array = [int(number) for number in input().split()]
    print(broken_search(array, target))
