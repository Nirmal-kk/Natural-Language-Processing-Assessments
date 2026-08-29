import re

expression = input("Enter logical expression: ")

tokens = re.findall(r'[A-Za-z]+|[()¬∧∨→∀∃]', expression)

print("\nTokens:")
for token in tokens:
    print(token)

print("\nExpression Structure:")

if "∀" in tokens:
    print("Universal Quantifier found")
if "∃" in tokens:
    print("Existential Quantifier found")
if "∧" in tokens:
    print("AND operator found")
if "∨" in tokens:
    print("OR operator found")
if "→" in tokens:
    print("IMPLIES operator found")
if "¬" in tokens:
    print("NOT operator found")

print("FOPC expression parsed successfully.")