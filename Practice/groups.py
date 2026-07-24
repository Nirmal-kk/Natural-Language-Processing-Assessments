import re
m = re.search(r"(\w+) (\d+)", "Age 21")
print(m.groups())
