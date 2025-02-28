import re

text = input("Enter the string: ")
pattern = r'(?<!^)(?=[A-Z])'
split_word = re.sub(pattern, "_", text).lower()
print(split_word)







# to convert a given camel 
# case string to snake case.




# (?<!^) – Отрицательный просмотр назад (negative lookbehind).
# Гарантирует, что _ не будет вставлен перед первой буквой строки.
# (?=[A-Z]) – Позитивный просмотр вперед (positive lookahead).
# Находит все заглавные буквы, перед которыми нужно вставить _.