import re
def remove_parentheses(text):
    text = re.sub("\(.*?\)", "", text)
    print(text)
