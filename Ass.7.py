import re

# Sample text
text = """
Please contact us at john@example.com or support@gmail.com.
You can also email admin@college.edu.in for further information.
"""

# Regular expression pattern for email addresses
pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# Find all email addresses
emails = re.findall(pattern, text)

# Display the results
print("Email addresses found:")

for email in emails:
    print(email)