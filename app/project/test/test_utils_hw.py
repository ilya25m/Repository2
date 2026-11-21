from project.utils import calculate_discount, is_even, get_full_name

def test_calculate_discount_20():
    assert calculate_discount(100, 20) == 80

def test_calculate_discount_50():
    assert calculate_discount(200, 50) == 100

def test_calculate_discount_0():
    assert calculate_discount(150, 0) == 150

def test_calculate_discount_zero_price():
    assert calculate_discount(0, 20) == 0

def test_calculate_discount_other():
    assert calculate_discount(300, 10) == 270

def test_is_even_positive():
    assert is_even(4) is True

def test_is_even_odd():
    assert is_even(7) is False

def test_is_even_negative():
    assert is_even(-6) is True

def test_is_even_negative_odd():
    assert is_even(-5) is False

def test_is_even_zero():
    assert is_even(0) is True

def test_get_full_name_normal():
    assert get_full_name("Ilya", "Misiura") == "Ilya Misiura"

def test_get_full_name_short():
    assert get_full_name("Al", "Li") == "Al Li"

def test_get_full_name_long():
    assert get_full_name("Kirril", "Zverev") == "Kirril Zverev"

def test_get_full_name_one_character():
    assert get_full_name("A", "B") == "A B"

def test_get_full_name_other():
    assert get_full_name("Ivan", "Ivanov") == "Ivanov Ivanov"
