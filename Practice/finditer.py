import re
text = "123 456 789"
for match in re.finditer(r"\d+", text):
    print(match.group(), match.start())
