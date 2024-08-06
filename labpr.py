# List of strings
strings = ["apple", "banana", "cherry", "date", "elderberry"]

# Initialize an empty list to hold matches
matches = []

# Condition: Collect strings that contain the letter 'a'
for s in strings:
    if 'a' in s:
        matches.append(s)

# Print the matches list
print(matches)
