from translate import Translator
import datetime
import random


class LanguageBot:
    def __init__(self):
        self.translator = Translator(to_lang='ru')

    def translate(self, text):
        """Переводит текст с одного языка на другой."""
        translation = self.translator.translate(text)
        return translation

    def daily_exercise(self, language):
        """Предлагает ежедневное упражнение на заданном языке."""
        exercise_types = {
            "translation": "Перевести фразу",
            "vocabulary": "Заучить новые слова",
            "reading": "Прочитать текст"
        }

        exercise_type = random.choice(list(exercise_types.keys()))
        print(f"Сегодняшнее упражнение: {exercise_types[exercise_type]}")

        if exercise_type == "translation":
            phrase = "Greetings to you, the user of my software." 
            translation = self.translate(phrase)
            print(f"Переведите фразу: {phrase}")
            print(f"Перевод: {translation}")
        elif exercise_type == "vocabulary":
            word_list = ["hello", "world", "good", "morning"] 
            word = random.choice(word_list)
            translation = self.translate(word)
            print(f"Заучите слово: {word}")
            print(f"Перевод: {translation}")
        elif exercise_type == "reading":
            text = ("Python is a powerful and flexible programming language that is widely used in various fields such as data science,"
                    " machine learning, web development and automation. It is known for its simple and understandable syntax,"
                    " which makes it an excellent choice for both beginners and experienced developers."
                    " Python offers a rich ecosystem of libraries and frameworks that simplify the development of complex applications.") 
            print(f"Прочитайте текст: {text}")

    def set_reminder(self, time, message):
        """Устанавливает напоминание."""
        now = datetime.datetime.now()
        try:
            reminder_time = datetime.datetime.strptime(time, "%H:%M")
        except ValueError:
            print("Неверный формат времени. Используйте формат ЧЧ:ММ.")
            return

        if reminder_time < now:
            reminder_time += datetime.timedelta(days=1)
        print(f"Напоминание установлено на {time}: {message}")

    def main(self):
        """Главная функция бота."""
        while True:
            print("Выберите действие:")
            print("1. Перевести текст")
            print("2. Получить ежедневное упражнение")
            print("3. Установить напоминание")
            print("4. Выйти")

            choice = input("Введите номер действия: ")

            if choice == "1":
                lang = [
                    'RU', 'EN'
                ]
                url = "https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes"

                question = input("На какой язык хотите перевети? ")
                if question not in lang:
                    print(f"Чтобы правильно ввести язык ознакомьтесь с кодами языков : {url}")

                text = input("Введите текст для перевода: ")
                translation = self.translate(text)
                print(f"Перевод: {translation}")

            elif choice == "2":
                lang = [
                    'RU', 'EN'
                ]
                url = "https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes"
                language = input("Введите язык для упражнения: ")
                if language not in lang:
                    print(f"Чтобы правильно ввести язык ознакомьтесь с кодами языков : {url}")
                self.daily_exercise(language)

            elif choice == "3":
                time = input("Введите время для напоминания (ЧЧ:ММ): ")
                message = input("Введите сообщение для напоминания: ")
                self.set_reminder(time, message)

            elif choice == "4":
                break
            else:
                print("Неверный выбор.")


if __name__ == "__main__":
    bot = LanguageBot()
    bot.main()
