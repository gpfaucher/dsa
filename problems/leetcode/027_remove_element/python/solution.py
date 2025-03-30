def solution(nums: list[int], val: int) -> int:
    k = list(filter(lambda x: x != val, nums))

    for i, x in enumerate(k):
        nums[i] = x

    if len(k) == 1:
        return k[0]

    return len(k)


def test_tiny():
    assert solution([2, 2, 3], 2) == 3


def test_short():
    assert solution([3, 2, 2, 3], 3) == 2


def test_long():
    assert solution([0, 1, 2, 2, 3, 0, 4, 2], 2) == 5
