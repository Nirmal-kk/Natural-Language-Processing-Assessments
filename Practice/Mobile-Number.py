import re
mobile = input("Enter mobile number: ")
pattern = r"^(?:\+91|91)?[6-9]\d{9}$"
if re.fullmatch(pattern, mobile):
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")
