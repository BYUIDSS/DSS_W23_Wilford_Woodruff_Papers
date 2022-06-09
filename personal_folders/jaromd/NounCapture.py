import re

with open('derived_data\journals.txt') as journals_file:
    text = journals_file.read()

def get_nouns(text):
    # Pattern to grab nouns formatted as "[[NOUN ...|"
    pattern = r"\[\[.+?\|"
    # People and place lists initialized
    clean_place = []
    clean_people = []
    # The nouns are captured from given text.
    captured = re.findall(pattern, text)

    # The nouns are cleaned of brackets and 
    for noun in captured:
        clean_noun = noun.strip("[|")
        if "," in clean_noun:
            if ", b." in clean_noun:
                clean_people.append(clean_noun)
            else:
                clean_place.append(clean_noun)
        else:
            clean_people.append(clean_noun)
    
    return [clean_place, clean_people]


