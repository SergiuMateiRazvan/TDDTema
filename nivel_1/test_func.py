import pytest

from func import get_no_of_equals


@pytest.mark.parametrize(
    "elements, element, expected",
    [([1, 2, 3, 4, 5, 3, 4, 2, 7, 4], 4, 3), ([1, 2], 1, 1), ([1, 1, 1, 1], 1, 4)],
)
def test_get_no_of_equals(elements, element, expected):
    assert get_no_of_equals(elements, element) == expected


@pytest.mark.parametrize(
    "elements, element", [([1, 2, 3, 4, 5, 3, 4, 2, 7, 4], 8), ([2], 1), ([], 1)]
)
def test_get_no_of_equals_not_found(elements, element):
    with pytest.raises(Exception):
        get_no_of_equals([1, 2, 3], 9)
