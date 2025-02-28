import re

text = input("Enterthe string: ")
pattern = r'(?<!^)(?=[A-Z])'
result = re.sub(pattern, " ", text)
print(result)





# to insert spaces between words 
# starting with capital letters.



# (?<!^) – Отрицательный просмотр назад (negative lookbehind).
# Гарантирует, что замена не будет происходить в самом начале строки.
# (?=[A-Z]) – Позитивный просмотр вперед (positive lookahead).
# Находит все заглавные буквы, перед которыми нужно вставить пробел.
 
