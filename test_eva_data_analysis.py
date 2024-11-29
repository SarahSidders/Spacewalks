from src.eva_data_analysis import calculate_crew_size, text_to_duration
import pytest


def test_text_to_duration_integer():
    """
    Test that text_to_duration returns expected ground truth values
    for typical whole hour durations 
    """
    input_value = "10:00"
    assert text_to_duration(input_value) == 10

def test_text_to_duration_float_quarter_of_an_hour():
    """
    Test that text_to_duration returns expected ground truth values
    for typical durations with a non-zero minute component
    """
    input_value = "10:15"
    assert text_to_duration(input_value) == 10.25

def test_text_to_duration_a_third_of_an_hour():
    """
    Test that text_to_duration returns expected ground truth values
    for typical durations with a non-zero minute component
    """
    input_value = "10:20"
    assert text_to_duration(input_value) == pytest.approx(10.333333)

@pytest.mark.parametrize("input_value, expected_result", [
    ("Steve;", 1),
    ("Bob; Steve", 2),
    ("", None)
])

def test_calculate_crew_size_returns_the_correct_numbers(input_value, expected_result):
    """
    Test that calculate_crew_size returns the expected crew size values.
    """
    actual_result = calculate_crew_size(input_value)
    actual_result == expected_result

    actual_result = calculate_crew_size(input_value)
    actual_result == expected_result

def test_calculate_crew_size_returns_None_if_empty():
    """
    Test that calculate_crew_size returns the expected None value when the string is empty.
    """
    input_value = ""
    actual_result = calculate_crew_size(input_value))
    expected_result = None
    actual_result == expected_result
