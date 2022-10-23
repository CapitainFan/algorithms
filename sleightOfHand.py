def calculations(k: int, function_matrix: list) -> int:
    numbers = {}

    for i in function_matrix:
        if i != '.':
            numbers[int(i)] = numbers[int(i)] + 1 if int(i) in numbers else 1

    score = 0

    for number, count in numbers.items():
        score += 1 if count <= k else 0

    return score


def main() -> None:
    key_count = int(input()) * 2
    matrix = ''.join([input() for _ in range(4)])
    result = calculations(key_count, matrix)
    print(result)


if __name__ == "__main__":
    main()
