import re

text_to_match = input("Enter the string : ")
pattern = re.compile(r'[ ,.]')
replaced_text = pattern.sub(':', text_to_match)
print("Result:", replaced_text)








# to replace all occurrences of space, 
# comma, or dot with a colon.