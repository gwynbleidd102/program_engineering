import re

def is_correct_mobile_phone_number_ru(number: str) -> bool:
    # Убираем все пробелы, дефисы и скобки для более простой проверки
    clean_number = re.sub(r'[\s()-]', '', number)
    
    # Проверка на правильное начало номера
    if not clean_number.startswith(('8', '+7')):
        return False
    
    # Если номер начинается с 7, он должен начинаться с +7
    if clean_number.startswith('7') and not number.startswith('+7'):
        return False
    
    # Номер должен быть длиной 11 цифр для 8 и 12 цифр для +7
    if (number.startswith('+7') and len(clean_number) != 12) or (number.startswith('8') and len(clean_number) != 11):
        return False
    
    # Проверка соответствия шаблону
    pattern = r"^(\+7|8)?\d{10}$"
    return re.match(pattern, clean_number) is not None

if __name__ == "__main__":
    number = input().strip()
    if is_correct_mobile_phone_number_ru(number):
        print("YES")
    else:
        print("NO")
