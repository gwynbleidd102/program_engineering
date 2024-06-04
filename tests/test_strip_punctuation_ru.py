import pytest
from src.strip_punctuation_ru import strip_punctuation_ru

def test_strip_punctuation_ru():
    assert strip_punctuation_ru("Привет, мир!") == "Привет мир"
    assert strip_punctuation_ru("Как дела?") == "Как дела"
    assert strip_punctuation_ru("Это тестовый текст.") == "Это тестовый текст"
    assert strip_punctuation_ru("Никаких знаков!") == "Никаких знаков"
    assert strip_punctuation_ru("") == ""

if __name__ == "__main__":
    pytest.main()
