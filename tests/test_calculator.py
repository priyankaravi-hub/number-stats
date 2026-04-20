import pytest
import allure
from stats.calculator import mean, median, mode


@allure.feature("Mean")
@allure.story("Basic calculation")
def test_mean_basic():
    assert mean([1, 2, 3, 4, 5]) == 3.0


@allure.feature("Mean")
@allure.story("Error handling")
def test_mean_empty_raises():
    with pytest.raises(ValueError):
        mean([])


@allure.feature("Median")
@allure.story("Odd-length list")
def test_median_odd():
    assert median([3, 1, 2]) == 2


@allure.feature("Median")
@allure.story("Even-length list")
def test_median_even():
    assert median([1, 2, 3, 4]) == 2.5


@allure.feature("Mode")
@allure.story("Basic calculation")
def test_mode_basic():
    assert mode([1, 2, 2, 3]) == 2
