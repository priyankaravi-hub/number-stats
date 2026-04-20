import pytest
from stats.calculator import mean, median, mode

def test_mean_basic():
    assert mean([1, 2, 3, 4, 5]) == 3.0

def test_mean_empty_raises():
    with pytest.raises(ValueError):
        mean([])

def test_median_odd():
    assert median([3, 1, 2]) == 2

def test_median_even():
    assert median([1, 2, 3, 4]) == 2.5

def test_mode_basic():
    assert mode([1, 2, 2, 3]) == 2
