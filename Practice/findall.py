import re
text = "Cat Bat Rat Mat"
words = re.findall(r"\w+at", text)
print(words)
