from translate import Translator

def validate_input(input_text, input_type):
    """Проверяет ввод на пустоту и корректность"""
    if not input_text:
        print(f"{input_type} не может быть пустым. Пожалуйста, попробуйте еще раз.")
        return False
    return True

def translate_text():
    """Переводит текст введенный пользователем"""
    url = 'https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes'
    print('На данный момент переводчик работает на 145 языках')

    text = input('Введите слово или фразу: ')
    if not validate_input(text, "Текст"):
        return

    source_lang = input("На каком языке написан текст? (Код языка): ")
    if not validate_input(source_lang, "Язык"):
        return

    target_lang = input("На какой язык хотите перевести? (Код языка): ")
    if not validate_input(target_lang, "Язык"):
        return

    try:
        translator = Translator(from_lang=source_lang, to_lang=target_lang)
        translation = translator.translate(text)
        print(f"Перевод: {translation}")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
        print(f"Пожалуйста, убедитесь, что вы ввели корректные коды языков. Список кодов языков: {url}")

translate_text()
