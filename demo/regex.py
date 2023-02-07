import re

pattern = re.compile(r"([a-z]+)")  # compiles re object for pattern
matches = pattern.finditer("my-string") # searches for regex matches in given string

for match in matches:
    print(match)

print(re.search(pattern,"my-string"))

