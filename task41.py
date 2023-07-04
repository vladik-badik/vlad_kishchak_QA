import pytest
from pixel_with_defects import Pixel


def test_pixel_constructor_valid_components():
    # Валідні компоненти пікселя не повинні викликати виняток
    try:
        Pixel(0, 0, 0)
    except ValueError:
        pytest.fail("Valid pixel components raised ValueError unexpectedly.")

    try:
        Pixel(255, 255, 255)
    except ValueError:
        pytest.fail("Valid pixel components raised ValueError unexpectedly.")


def test_pixel_constructor_invalid_components():
    # Невалідні компоненти пікселя повинні викликати помилку ValueError
    with pytest.raises(ValueError):
        Pixel(-1, 0, 0)

    with pytest.raises(ValueError):
        Pixel(0, 256, 0)

    with pytest.raises(ValueError):
        Pixel(0, 0, -1)


def test_pixel_addition():
    pixel1 = Pixel(100, 50, 75)
    pixel2 = Pixel(50, 75, 100)

    result = pixel1 + pixel2

    assert result.r == 150
    assert result.g == 125
    assert result.b == 175


def test_pixel_subtraction():
    pixel1 = Pixel(100, 50, 75)
    pixel2 = Pixel(50, 75, 100)

    result = pixel1 - pixel2

    assert result.r == 50
    assert result.g == 0
    assert result.b == 0


def test_pixel_multiplication():
    pixel = Pixel(100, 50, 75)

    result = pixel * 2

    assert result.r == 200
    assert result.g == 100
    assert result.b == 150


def test_pixel_division():
    pixel = Pixel(100, 50, 75)

    result = pixel / 2

    assert result.r == 50
    assert result.g == 25
    assert result.b == 37


def test_pixel_multiplication_invalid_value():
    pixel = Pixel(100, 50, 75)

    # Множення  нечислових значеннь має викликати TypeError
    with pytest.raises(TypeError):
        pixel * "2"


def test_pixel_multiplication_invalid_multiplicator():
    pixel = Pixel(100, 50, 75)

    # Множення з нульовим або від’ємним множником має показати ерор ValueError
    with pytest.raises(ValueError):
        pixel * 0

    with pytest.raises(ValueError):
        pixel * -1


def test_pixel_equality():
    pixel1 = Pixel(100, 50, 75)
    pixel2 = Pixel(100, 50, 75)
    pixel3 = Pixel(200, 100, 150)

    assert pixel1 == pixel2
    assert pixel1 != pixel3


def test_pixel_str_representation():
    pixel = Pixel(100, 50, 75)

    result = str(pixel)

    expected = "Pixel object\n\tRed: 100\n\tGreen: 50\n\tBlue: 75\n"
    assert result == expected


def test_pixel_repr_representation():
    pixel = Pixel(100, 50, 75)

    result = repr(pixel)

    expected = "Pixel(100, 50, 75)"
    assert result == expected


def test_pixel_get_pixel_near():
    pixel = Pixel(100, 100, 100)

    result = pixel.get_pixel_near(10)

    assert 90 <= result.r <= 110
    assert 90 <= result.g <= 110
    assert 90 <= result.b <= 110


def test_pixel_coverage():
    assert pytest.approx(pytest.coverage.pytest_coverage(file="./pixel_with_defects.py"), 90)
