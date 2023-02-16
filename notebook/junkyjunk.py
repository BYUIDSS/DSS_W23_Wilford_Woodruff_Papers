
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
    
for i in topics_list:
    filtered_dataframe, clean = findPlace_topics(clean, i)

print(filtered_dataframe.head(5))
print(clean["topics"][154])


print(clean.head(10))

