import re

text_to_match = input("Enter the string: ")
pattern = re.compile(r'[A-Z][a-z]+')
matches = pattern.findall(text_to_match)
print("Matches:", matches)






# to find the sequences of one upper 
# case letter followed by lower case letters.