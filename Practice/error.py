import re
try:
    re.compile(r"[")
except re.error as e:
    print("Regex Error:", e)
