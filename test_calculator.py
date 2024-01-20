import pytest
from Calculator import calculator
from CalculatorException import CalculatorException


def test_syntax_errors():
    with pytest.raises(CalculatorException):
        calculator("3 ^ * 2")
    with pytest.raises(CalculatorException):
        calculator("3.32.2")
    with pytest.raises(CalculatorException):
        calculator("3 &")
    with pytest.raises(CalculatorException):
        calculator("(2) 5")
    with pytest.raises(CalculatorException):
        calculator("3 * (2 + 4")


def test_gibberish():
    with pytest.raises(CalculatorException):
        calculator("3r;)")


def test_empty_string():
    with pytest.raises(CalculatorException):
        calculator("")


def test_whitespace_string():
    with pytest.raises(CalculatorException):
        calculator("  \t ")


def test_simple_expressions():
    assert calculator("2. ^ 3") == 8
    assert calculator("5 - 10") == -5
    assert calculator("2 + 1.6") == 3.6
    assert calculator("-5 * 3") == -15
    assert calculator("10 / 2") == 5
    assert calculator("2 @ -2") == 0
    assert calculator(".2 $ -2") == 0.2
    assert calculator("2 & -.2") == -0.2
    assert calculator("7 % 3") == 1
    assert calculator("~-.3") == 0.3
    assert calculator("3!!") == 720
    assert calculator("99##") == 9
    assert calculator("---3 ^ 2") == -9
    assert calculator("2 + --3!") == 8
    assert calculator("5 - ---2") == 7


def test_complex_expressions():
    assert calculator("~(100 / 2 @ 4! % 2) * 9 $ 3! ^ 2") == -8100
    assert calculator("-10 $ (8 & (4 @ 9))# / ---11 + .5") == 1.5
    assert calculator("(4 + 8)#! * (6! - -4 ^ 4 - 4 * 100) ^ 0.5") == 48
    assert calculator("(5 ^ ~-14 & 4! % 3) $ -(-4 ^ 2 * 1.5)") == 25
    assert calculator("-5! @ ((-3 ^ 3) & -(18#)) * 5.24") == -243.66
    assert calculator("5.5 * 412 % 20 / -(~3 ^ --3 - --(---4 ^ 2))") == 6
    assert calculator("5! / (3 $ (2.6 * 11.2) - 4!) * ((~11 ^ 2)# - .5)") == 82.03125
    assert calculator("(((5 ^ 2 + 3 * 4) / (2 - 1)) ^ 3) % 231") == 64
    assert calculator("3.14 * (2.54 ^ 3 - 1.96) + 7.2 % 4.8") == 47.70098096
    assert calculator("8 ^ 8!# @ 19 * (12 ^ 2 / 100) ^ 0.5") == 5277655813324.8
    assert calculator("((8 * (1638.4 * 5) $ 8000) ^ 0.25)! / 1.2") == 17435658240000
    assert calculator("---7 & (0.6 / 2.5) * 2.3 ^ (~2 * -2 - -1)") == -15.4472232
    assert calculator("12 & 3! * 32# % 3 + ~--11 @ 32 - 3 $ 2") == 19.5
    assert calculator("4 ^ (4! & --6!#) @ (44 % 3 - 3)") == 256
    assert calculator("33 $ (21 & -----25) % 4 - 4 * 2 / 8") == 0
