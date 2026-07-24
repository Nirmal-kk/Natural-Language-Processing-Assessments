import re
pattern = re.compile(r"\d+")
print(pattern.findall("12 34 56"))
print(pattern.search("Age 19"))
print(pattern.match("123abc"))
print(pattern.fullmatch("123"))
print(pattern.split("12abc34"))
print(pattern.sub("#", "12abc34"))
