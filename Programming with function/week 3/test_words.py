"""Verify that the prefix and suffix functions work correctly."""

from words import prefix, suffix
import pytest


def test_prefix():
    """Verify that the prefix function works correctly.
    Parameters: none
    Return: nothing
    """
    # Call the prefix function and verify that it returns a string.
    pre = prefix("upbeat", "upgrade")
    assert isinstance(pre, str), "prefix function must return a string"

    # Call the prefix function ten times and use an assert
    # statement to verify that the string returned by the
    # prefix function is correct each time.
    assert prefix("cat", "catalog") == "cat"
    assert prefix("", "") == ""
    assert prefix("", "correct") == ""
    assert prefix("clear", "") == ""
    assert prefix("happy", "funny") == ""
    assert prefix("cat", "catalog") == "cat"
    assert prefix("dogmatic", "dog") == "dog"
    assert prefix("jump", "joyous") == "j"
    assert prefix("upbeat", "upgrade") == "up"
    assert prefix("Disable", "dIstasteful") == "dis"

def test_suffix():
    # sur = suffix("found", "profound")
    # assert isinstance(sur, str)

    assert suffix(" ", " ") == " "
    assert suffix(" ", "Correct ") == " "
    assert suffix("Clear ", " ") == " "
    assert suffix("Angelic ", "Awesome ") == " "
    assert suffix("Found ", "Profound ") == "found "
    assert suffix("Ditch ", "Itch ") == "itch "
    assert suffix("Happy ", "Funny ") == "y "
    assert suffix("Tired ", "Fatigued ") == "ed "
    assert suffix("Swimming ", "Flying ") == "ing "


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
