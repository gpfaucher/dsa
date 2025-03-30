def solution(s: str):
    romanValues = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    chars = list(s)
    result = 0
    prev = 0

    for char in reversed(chars):
        curr = romanValues[char]

        if curr < prev:
            result -= curr
        else:
            result += curr

        prev = curr

    return result


def test_single_digits():
    assert solution("III") == 3


def test_less_than_hundred():
    assert solution("LVIII") == 58


def test_thousands():
    assert solution("MCMXCIV") == 1994
