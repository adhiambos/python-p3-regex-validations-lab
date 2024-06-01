import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

name = r"\b\w+\b"
name_regex = re.compile(name)
for string in name:
    match = name_regex.match("John" "Cena")
    if match:
        print(match)
    else:
        print("no match")

phone_number = r"\d{3}-?\d{3}-?\d{4}"
phone_regex = re.compile(phone_number)

email_address = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,3}"
email_regex = re.compile(email_address)
