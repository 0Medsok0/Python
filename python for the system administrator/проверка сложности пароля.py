import re

def check_password_strength(password):
    # Проверка длины пароля
    if len(password) < 8:
        return "Password is too short"

    # Проверка наличия цифр
    if not re.search(r"\d", password):
        return "Password should contain at least one digit"

    # Проверка наличия букв в верхнем и нижнем регистре
    if not re.search(r"[A-Z]", password) or not re.search(r"[a-z]", password):
        return "Password should contain both uppercase and lowercase letters"

    # Проверка наличия специальных символов
    if not re.search(r"\W", password):
        return "Password should contain at least one special character"

    return "Password is strong"

# Пример использования функции
password = input("Enter your password: ")
print(check_password_strength(password))
