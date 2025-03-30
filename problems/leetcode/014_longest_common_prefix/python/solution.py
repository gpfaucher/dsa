def solution(strs: list[str]) -> str:
    x = strs[0]

    for y in range(1, len(strs)):
        while x and not strs[y].startswith(x):
            x = x[:-1]

    return x


def test_working_output():
    assert solution(["flower", "flow", "flight"]) == "fl"


def test_null():
    assert solution(["dog", "racecar", "car"]) == ""
