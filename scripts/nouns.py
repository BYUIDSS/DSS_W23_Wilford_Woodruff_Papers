import pandas as pd
import re

wwp = pd.read_csv("derived_data/journal_sentiments.csv")

def get_nouns(text):
    # Pattern to grab nouns formatted as "[[NOUN ...|"
    pattern = r"\[\[.+?\|"
    # People and place lists initialized
    clean_places = []
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
                clean_places.append(clean_noun)
        else:
            clean_people.append(clean_noun)
    
    return [clean_people, clean_places]

wwp['Nouns'] = wwp['entry'].map(get_nouns)

nouns_df = pd.DataFrame(wwp['Nouns'].tolist(), columns=['People', 'Places'])
wwp = pd.concat([wwp, nouns_df], axis=1)
wwp.drop(columns = ['Nouns'], inplace = True)
def cleaning_data(text):
 a2 = text.replace('[[','').replace(']]','').replace('[figure','').replace(']','')
 return a2
wwp.to_csv("derived_data/journals.csv")
wwp['entry'] = wwp['entry'].map(cleaning_data)