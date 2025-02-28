import re

text_to_match = input("Enter the string: ")
pattern = re.compile(r'\b[a-z]+_[a-z]+\b')
matches = pattern.findall(text_to_match)
print("Matches:", matches)




# to find sequences of lowercase letters 
# joined with a underscore.

