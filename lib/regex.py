import re

def match_lovely_day(text):
    # Pattern to match the string "It's such a lovely day today."
    pattern = r"It's such a lovely day today\."
    
    # Using re.match to check if the pattern matches the text
    return re.match(pattern, text)

def match_chosen_table(text):
    # Pattern to match the string "You have chosen a table"
    pattern = r"You have chosen a table"
    
    # Using re.search to check if the pattern is present in the text
    return re.search(pattern, text)
