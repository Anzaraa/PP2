import re

text_to_match = input("Enter the string: ")
pattern = re.compile(r'^ab{2,3}$')
result = pattern.fullmatch(text_to_match)
if result:
    print("Match!")
else:
    print("No match!")




# matches a string that has 
# an 'a' followed by two to three 'b'.