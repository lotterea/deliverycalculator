import pytest

from delivery_calculator.delivery_calculator import calculate_delivery_cost

test_cases = [
    [1.0, "small", False, "normal", 400],
    [1, "small", False, "normal", 400],
    [2, "large", True, "normal", 550],
    [9, "large", False, "increased", 400],
    [10, "small", True, "increased", 600],
    [11, "small", True, "high", 840],
    [20, "large", False, "high", 560],
    [21, "large", False, "very high", 640],
    [30, "small", True, "very high", 960],
    [31, "small", False, "very high", 640],
    [31, "large", False, "high", 700],
    [30, "large", False, "high", 560],
    [21, "small", True, "high", 840],
    [20, "small", True, "very high", 960],
    [11, "large", False, "very high", 640],
    [10, "large", False, "very high", 480],
    [9, "small", True, "very high", 800],
    [2, "small", False, "very high", 400],
    [1, "large", True, "very high", 880],
    [31, "large", False, "increased", 600],
    [31, "large", False, "normal", 500],
    [1, "large", False, "high", 400],
    [2, "large", False, "high", 400],
    [9, "large", False, "high", 420],
    [10, "large", False, "high", 420],
    [11, "large", False, "normal", 400],
    [20, "large", False, "normal", 400],
    [21, "large", False, "normal", 400],
    [30, "large", False, "normal", 400],
]


def generate_test_id(param):
    distance, size, fragile, workload, expected = param
    return f"{distance} km, {size}, {'fragile' if fragile else 'not fragile'}, {workload} workload, expected {expected} RUB"


@pytest.mark.parametrize(
    "distance, size, fragile, workload, expected",
    test_cases,
    ids=map(generate_test_id, test_cases),
)
def test_calculate_delivery_cost(distance, size, fragile, workload, expected):
    assert calculate_delivery_cost(distance, size, fragile, workload) == expected


@pytest.mark.parametrize(
    "distance, size, fragile, workload, expected_exception, expected_message",
    [
        (
            35,
            "small",
            True,
            "normal",
            ValueError,
            "Fragile items cannot be delivered on a distance greater than 30 km",
        ),
        (-5, "small", False, "normal", ValueError, "Distance must be more than 0"),
        (0, "small", False, "normal", ValueError, "Distance must be more than 0"),
        ("0", "small", False, "normal", TypeError, "Distance must be int or float"),
        (5, "medium", False, "normal", ValueError, "Invalid size"),
        (5, "small", False, "extremely high", ValueError, "Invalid workload"),
        (
            15,
            "small",
            "fragile",
            "normal",
            TypeError,
            "fragile parameter must be a boolean",
        ),
    ],
)
def test_negative_calculate_delivery_cost(
    distance, size, fragile, workload, expected_exception, expected_message
):
    with pytest.raises(expected_exception) as excinfo:
        calculate_delivery_cost(distance, size, fragile, workload)
    assert str(excinfo.value) == expected_message
