import pytest
from fairsharer_function import fair_sharer


def test_wrapping():
    # Input designed to test wrapping logic
    values = [0, 0, 800, 1000]  # Max value is at the last index
    num_iterations = 1
    share = 0.1

    # Expected result after one iteration
    # 1000 gives 100 (10%) to both the neighbors (index 2 and index 0)
    expected_values = [100, 0, 900, 800]

    # Run the fair_sharer function
    result = fair_sharer(values, num_iterations, share)

    # Assert the wrapping works as intended
    assert result == expected_values


def test_fair_sharer_result():
    assert fair_sharer([0, 1000, 800, 0], 1) == [100, 800, 900, 0]
    assert fair_sharer([0, 1000, 800, 0], 2) == [100, 890, 720, 90]
