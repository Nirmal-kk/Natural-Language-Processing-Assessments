import re
text = "one one one"
result = re.subn(r"one", "two", text)
print(result)
