import re
pattern = re.compile(r"\d+")
text = "Age: 19"
match = pattern.search(text)
print(match.group())
