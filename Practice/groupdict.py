import re
m = re.search(r"(?P<name>\w+) (?P<age>\d+)", "John 20")
print(m.groupdict())
