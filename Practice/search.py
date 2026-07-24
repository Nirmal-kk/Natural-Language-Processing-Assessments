import re
text = "I love Python"
result = re.search(r"Python", text)
if result:
    print("Found at index:", result.start())
