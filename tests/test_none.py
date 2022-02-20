"""Created for fix crash mypy with:
"There are no .py[i] files in directory 'tests'".
"""


def test_always_true() -> None:
    """Just placeholder for pytest work without tests."""
    assert True
