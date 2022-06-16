import re

with open('derived_data\journals.txt') as journals_file:
    text = journals_file.read()

def get_nouns(text):

    '''
    get_nouns goes through the given text to find nouns formatted as [ FORMAL NOUN | Wilford Woodruff's original writing].
    It then strips unneccesary items to just get the formal noun, and returns a list of a list of people and a list of places.
    '''

    # Pattern to grab nouns formatted as "[[NOUN ...|"
    pattern = r"\[\[.+?\|"
    # People and place lists initialized
    clean_place = []
    clean_people = []
    # The nouns are captured from given text.
    captured = re.findall(pattern, text)

    # The nouns are cleaned of brackets and the pipe symbol and split into people and places.
    for noun in captured:
        # Unneeded symbols are stripped.
        clean_noun = noun.strip("[|")
        # Nouns with commas are seperated.
        if "," in clean_noun:
            # If they have the ", .b" the noun is a person but has a birthdate.
            if ", b." in clean_noun:
                clean_people.append(clean_noun)
            # If it doesn't it is a place.
            else:
                clean_place.append(clean_noun)
        # If there's no comma, it's a person.
        else:
            clean_people.append(clean_noun)
    
    return [clean_place, clean_people]


