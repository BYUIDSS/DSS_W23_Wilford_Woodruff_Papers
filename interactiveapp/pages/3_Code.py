import streamlit as st
import re
from nltk.metrics import edit_distance 
import pandas as pd
import pandas as pd
import numpy as np


def code():
    st.title("Code Showcase")

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
    wwp = pd.read_csv("https://raw.githubusercontent.com/BYUIDSconsulting/woodruff_stories/master/personal_folders/treylusk/WW_by_date.csv")
    st.subheader("Load in the dataset and topics")
    st.code('''
topics_list = ['repent', 'Family', 'Conference', 'Help','Death',
            'Fish','Apostle','Jesus','God','Holy Ghost',
            'Preisthood','Women','Agency','Accountability',
            'Depression','Encouragement','Hope','Mercy','Sorrow',
            'Baptism','Bible','Blessings','Brotherhood','Sisterhood',
            'Kingdom','Charity','Chasitity','Christmas',
            'Commandments','Commitment','Compassion','Consecration',
            'Courage','Creation','Diligence','Dicouragement',
            'Duty','Enduring','Etenal','Life','Exaltation',
            'Example','Fatherhood','Forgiveness','Gathering',
            'Israel','Temple','Temple Work','Goals',
            'Grace','Gospel','Gratitude','Guidance','Home'
]
wwp = pd.read_csv("https://raw.githubusercontent.com/BYUIDSconsulting/woodruff_stories/master/personal_folders/treylusk/WW_by_date.csv")
    ''','python')
    st.write("This is how we grabbed the topics and loaded in the data.")
    st.write("#### Data:")
    st.dataframe(wwp)
    st.subheader("Find Misspelled words")
    

    def find_misspelled(word):
        regex = '|'.join(['(' + re.escape(word[:i]) + '.' + re.escape(word[i+1:]) + ')' for i in range(len(word))])
        
        #Find words in the english3.txt files so we can 
        with open('notebook/english3.txt') as f:
            dictionary = set(word.strip().lower() for word in f)
        matches = [match.group() for match in re.finditer(regex, ' '.join(dictionary))]
        
        misspelled = [match for match in matches if edit_distance(match, word) <= 1]
        misspelled = sorted(list(set(misspelled)))
        return misspelled

    misspelled_words = dict()
    for topic in topics_list:
        misspelled_words[topic] = find_misspelled(topic)
    st.code('''
import re
from nltk.metrics import edit_distance 

def find_misspelled(word):
    regex = '|'.join(['(' + re.escape(word[:i]) + '.' + re.escape(word[i+1:]) + ')' for i in range(len(word))])
    
    #Find words in the english3.txt files so we can 
    with open('notebook/english3.txt') as f:
        dictionary = set(word.strip().lower() for word in f)
    matches = [match.group() for match in re.finditer(regex, ' '.join(dictionary))]
    
    misspelled = [match for match in matches if edit_distance(match, word) <= 1]
    misspelled = sorted(list(set(misspelled)))
    return misspelled

misspelled_words = dict()
for topic in topics_list:
    misspelled_words[topic] = find_misspelled(topic)
    
    ''','python')

    st.write('Using the english3.txt dictionary we find and locate a set of misspelled words then put it in a dictionary.')
    st.write("#### Misspelled Words")
    st.dataframe(misspelled_words)

    st.subheader('Cleaning Data')
    clean = (wwp
    .replace([-999, "", "NAN", "nan", "n/a", "NaN", np.nan], "")
    .replace("&amp;", "and")
    )

    for topic in topics_list:
        clean = (clean
            .replace(misspelled_words[topic], topic)
        )

    # add empty lists in new column named topics
    clean['topics'] = [[] for _ in range(len(clean))]
    st.code('''
clean = (wwp
    .replace([-999, "", "NAN", "nan", "n/a", "NaN", np.nan], "")
    .replace("&amp;", "and")
)

for topic in topics_list:
    clean = (clean
        .replace(misspelled_words[topic], topic)
    )

# add empty lists in new column named topics
clean['topics'] = [[] for _ in range(len(clean))]
    ''','python')
    st.write("#### Cleaned Data")
    st.dataframe(clean)
    st.subheader('More User Define Functions')

    def filter_my_data(pd_dataframe, filter_exp):
        return pd_dataframe.query('text.str.contains(@filter_exp)')


    def findPlace_topics(clean, topic):
        filtered_dataframe = filter_my_data(clean, topic)

        for index in filtered_dataframe.index:
            clean['topics'][index].append(topic)
        
        return filtered_dataframe, clean
    st.code('''
def filter_my_data(pd_dataframe, filter_exp):
    return pd_dataframe.query('text.str.contains(@filter_exp)')


def findPlace_topics(clean, topic):
    filtered_dataframe = filter_my_data(clean, topic)

    for index in filtered_dataframe.index:
        clean['topics'][index].append(topic)
    
    return filtered_dataframe, clean
    ''','python')
    
    st.write('Filter My Data function finds inside of dataframe if text contains topic')
    st.write('Find Place Topics functions takes the Filter My Data functions and appends topic to data')

    st.subheader('Find Topics')
    for i in topics_list:
        filtered_dataframe, clean = findPlace_topics(clean, i)
    st.code('''
for i in topics_list:
    filtered_dataframe, clean = findPlace_topics(clean, i)
    ''','python')

    st.write('### Topic Data')
    st.write('##### Filtered Data')
    st.dataframe(filtered_dataframe)
    st.write('##### Main Data')
    st.dataframe(clean, use_container_width=True)
    st.header('Summary')
    st.write('This is a script written in Python that performs text analysis on a dataset of personal stories. The script defines a list of topics, which are then used to filter the dataset for stories that mention these topics. The script also uses the NLTK library to identify misspelled words and correct them using a stemmer. Finally, the script adds a new column to the dataset called "topics," which contains a list of the topics mentioned in each story. The script outputs the filtered dataset and the new "topics" column.')
    

code()