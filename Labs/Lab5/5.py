import re

text_to_match = input("Enter the string : ")
pattern = re.compile(r'^a.*b$')
result = pattern.fullmatch(text_to_match)
if result:
    print("Match!")
else:
    print("No match!")





# matches a string that has an 'a' followed 
# by anything, ending in 'b'.