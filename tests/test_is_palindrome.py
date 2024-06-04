import pytest
from src.is_palindrome import is_palindrome

def test_is_palindrome():
    assert is_palindrome("madam") == True
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("step on no pets") == True
    assert is_palindrome("palindrome") == False

if __name__ == "__main__":
    pytest.main()
