from calculator.my_math import get_number, div_from_input
from pytest import MonkeyPatch


def test_get_number_recovers_from_bad_input(monkeypatch: MonkeyPatch):
    # fake keyboard inputs.
    fake_inputs = iter(["abc", "10"])

    def mock_input(prompt: str) -> str:
        return next(fake_inputs)

    # mock_input2: Callable[[str], str] = lambda prompt: next(fake_inputs)

    # We hijack the built-in input() function and tell it to use out list instead
    monkeypatch.setattr("builtins.input", mock_input)

    # Run the function. It should fail on "abc", loop again, and succeed on "10".
    result = get_number("Enter a number: ")
    assert result == 10.0


def test_div_normal_math(monkeypatch: MonkeyPatch):
    # Fake typing "10" for the first number, and "2" for the second
    fake_inputs = iter(["10", "2"])

    def mock_input(prompt: str) -> str:
        return next(fake_inputs)

    monkeypatch.setattr("builtins.input", mock_input)

    result = div_from_input()
    assert result == 5.0


def test_div_by_zero(monkeypatch: MonkeyPatch):
    # Fake typing "10" then "0"
    fake_inputs = iter(["10", "0"])

    def mock_input(prompt: str) -> str:
        return next(fake_inputs)

    monkeypatch.setattr("builtins.input", mock_input)

    result = div_from_input()

    # Based on your code, dividing by zero should return None
    assert result == None
