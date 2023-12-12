import re
text = "To be, or not to be, that is the question"
out = re.findall("[a-zA-Z]+", text)
print(len(out))