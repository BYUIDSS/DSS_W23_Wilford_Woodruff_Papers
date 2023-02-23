
import pandas as pd
import altair as alt
import numpy as np

from IPython.display import Markdown
from IPython.display import display
from tabulate import tabulate


topics_list = ['repent',
            'Family',
            'Conference',
            'Help',
            'Death',
            'Fish',
            'Apostle',
            'Jesus',
            'God',
            'Holy Ghost',
            'Preisthood',
            'Women',
            'Agency',
            'Accountability',
            'Depression',
            'Encouragement',
            'Hope',
            'Mercy',
            'Sorrow',
            'Baptism',
            'Bible',
            'Blessings',
            'Brotherhood',
            'Sisterhood',
            'Kingdom',
            'Charity',
            'Chasitity',
            'Christmas',
            'Commandments',
            'Commitment',
            'Compassion',
            'Consecration',
            'Courage',
            'Creation',
            'Diligence',
            'Dicouragement',
            'Duty',
            'Enduring',
            'Etenal',
            'Life',
            'Exaltation',
            'Example',
            'Fatherhood',
            'Forgiveness',
            'Gathering',
            'Israel',
            'Temple',
            'Temple Work',
            'Goals',
            'Grace',
            'Gospel',
            'Gratitude',
            'Guidance',
            'Home'
]

wwp = pd.read_csv("./notebook/wwp.csv")
wwp.rename(columns={"Text Only Transcript": "text_only_transcript"}, inplace=True)


clean = (wwp
    .replace([-999, "", "NAN", "nan", "n/a", "NaN", np.nan], "")
    .replace("&amp;", "and")
)

# add empty lists in new column named topics
clean['topics'] = [[] for _ in range(len(clean))]



def filter_my_data(pd_dataframe, filter_exp):
    return pd_dataframe.query('text_only_transcript.str.contains(@filter_exp)')


def findPlace_topics(clean, topic):
    filtered_dataframe = filter_my_data(clean, topic)

    for index in filtered_dataframe.index:
        clean['topics'][index].append(topic)
    
    return filtered_dataframe, clean
    

import re
from nltk.metrics import edit_distance 

def find_misspelled(word):
    regex = '|'.join(['(' + re.escape(word[:i]) + '.' + re.escape(word[i+1:]) + ')' for i in range(len(word))])
    
   
    with open('notebook\\english3.txt') as f:
        dictionary = set(word.strip().lower() for word in f)
    matches = [match.group() for match in re.finditer(regex, ' '.join(dictionary))]
    
    
    return [match for match in matches if edit_distance(match, word) <= 1]

misspelled_words = dict()
for topic in topics_list:
    misspelled_words[topic] = find_misspelled(topic)

print(misspelled_words)

for i in topics_list:
    filtered_dataframe, clean = findPlace_topics(clean, i)

print(filtered_dataframe.head(5))
print(clean["topics"][154])


print(clean.head(10))

print(clean.info())

clean.to_csv("C:\\Users\\tyler\\societies\\datascience\\ww_papers\\DSS_W23_Wilford_Woodruff_Papers\\notebook\\cleaned_wwp.csv")
