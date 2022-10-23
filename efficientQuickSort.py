# Id = 70860768
class Participant:
    def __init__(self, name: str, points: int, penalty: int) -> None:
        self.name = name
        self.points = int(points)
        self.penalty = int(penalty)

    def __str__(self) -> str:
        return self.name

    def __lt__(self, other) -> bool:
        return ((-self.points, self.penalty, self.name) <
                (-other.points, other.penalty, other.name))


def quicksort(array: list, left_index: int, right_index: int) -> None:
    if left_index >= right_index:
        return

    left, right = left_index, right_index
    pivot = array[(right + left) // 2]

    while left <= right:
        while array[left] < pivot:
            left += 1
        while array[right] > pivot:
            right -= 1
        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1

    quicksort(array, left_index, right)
    quicksort(array, left, right_index)


if __name__ == '__main__':
    players_count = int(input())
    players = [Participant(*input().split()) for _ in range(players_count)]
    quicksort(players, 0, players_count-1)
    print(*players, sep='\n')
