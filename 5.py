import re

pan = input("Enter PAN Number: ")

pattern = r"^[A-Z]{5}[0-9]{4}[A-Z]{1}"

if re.match(pattern, pan):
    print("Valid PAN Number")
else:
    print("Invalid PAN Number")