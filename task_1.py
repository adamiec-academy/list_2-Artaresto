import re
def remove_parentheses(text):
    text = re.sub("\(.*?\)\s+", "", text)
    print(text)
