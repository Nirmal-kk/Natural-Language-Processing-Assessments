import re
text = "Python is awesome"
result = re.match(r"Python", text)
if result:
    print("Matched:", result.group())
else:
    print("No match")
