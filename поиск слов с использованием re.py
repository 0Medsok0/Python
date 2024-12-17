import re

def search_keywords(filename, keywords):
  """
  Выполняет поиск ключевых слов в файле с помощью регулярных выражений.

  Аргументы:
    Имя файла: Путь к файлу для поиска.
    Ключевые слова: Список ключевых слов для поиска.

  Возвращается:
    Список кортежей, где каждый кортеж содержит ключевое слово и номер строки, в которой он был найден.
  """
  results = []
  with open(filename, 'r') as file:
    for line_number, line in enumerate(file, 1):
      for keyword in keywords:
        if re.search(keyword, line):
          results.append((keyword, line_number))
  return results

keywords_to_search = ['function', 'class', 'import']
file_to_search = 'your_file.py'
found_keywords = search_keywords(file_to_search, keywords_to_search)
print(f'Found keywords in {file_to_search}:')
for keyword, line_number in found_keywords:
  print(f'- {keyword} found on line {line_number}')
