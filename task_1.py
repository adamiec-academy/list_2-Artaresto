import re
def remove_parentheses(text):
    text = re.sub("\(.*?\)", "", text)
    print(text)

remove_parentheses("Possiblen't (nie) jest istniejącym słowem")
