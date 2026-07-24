import re
text = "Apple,Banana;Orange Mango"
result = re.split(r"[,; ]+", text)
print(result)
