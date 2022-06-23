from dataclasses import replace
from logging import PlaceHolder
from pickle import NONE
import re

#with open('derived_data\journals.txt') as journals_file:
    #text = journals_file.read()
text = '''10 Arose in the morning sumwhat ill in consequence of
the hard tower we endured the day previous[.] rode
to Elder [[Johnston F. Lane|J. F Lane]] to attend the counsel of Elders
to take into consideration the case of Sister 
[[Lucinda Benton|Bentons]] the following is the procedings of the court'''
clean_text_list = []
a1 = text
a2 = a1.replace('[[','').replace(']]','').replace('[FIGURE','').replace(']','')
clean_text_list.append(a2)
x = NONE
z = None
placeholder = ""
for i in text:
    if i == "|":
        z = i
    if x != "]" and z == "|":
        placeholder += i
        x = i
    elif x == "]":
        a2 = a1.replace(placeholder, "")
        clean_text_list.append(a2)
        placeholder = ""
        z = x
        print(clean_text_list)

def get_nouns(text):



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



