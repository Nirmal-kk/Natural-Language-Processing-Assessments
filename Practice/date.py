import re
date = input("Enter date (DD/MM/YYYY): ")
pattern = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$"
if re.fullmatch(pattern, date):
    print("Valid Date")
else:
    print("Invalid Date")
