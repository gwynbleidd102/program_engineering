import pytest
from is_correct_mobile_phone_number_ru import is_correct_mobile_phone_number_ru

def test_is_correct_mobile_phone_number_ru():
    assert is_correct_mobile_phone_number_ru("+7 999 123-45-67") == True
    assert is_correct_mobile_phone_number_ru("8(999)1234567") == True
    assert is_correct_mobile_phone_number_ru("89991234567") == True
    assert is_correct_mobile_phone_number_ru("+7 999 123 45 67") == True
    assert is_correct_mobile_phone_number_ru("9991234567") == False
    assert is_correct_mobile_phone_number_ru("7 999 123 45 67") == False
    assert is_correct_mobile_phone_number_ru("8 999 123 45 67") == True
    assert is_correct_mobile_phone_number_ru("8 999 123 45 6") == False
    assert is_correct_mobile_phone_number_ru("+7 (999) 123 45 67") == True
    assert is_correct_mobile_phone_number_ru("+7-999-123-45-67") == True
    assert is_correct_mobile_phone_number_ru("+7 999 123 45 678") == False

if __name__ == "__main__":
    pytest.main()
