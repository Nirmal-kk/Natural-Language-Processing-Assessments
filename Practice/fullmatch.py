import re
text = "9876543210"
result = re.fullmatch(r"\d{10}", text)
print(result is not None)
