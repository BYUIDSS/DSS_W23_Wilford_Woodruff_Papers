#%%
from urllib import response
import nltk 
nltk.download('punkt')
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
import pandas as pd
#%%
topics = ['Family',
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
real_data = pd.read_csv('C:\\Users\\tyler\\societies\\datascience\\ww_papers\\DSS_W23_Wilford_Woodruff_Papers\\notebook\\wwp.csv')

#%%
def stemmer_de_stem(stemming_data):
    data = [stemmer.stem(w.lower()) for w in stemming_data if w not in '?']

    return data

#%%
my_stem = stemmer_de_stem(topics)

#%%
print(my_stem)
#%%
real_data['text_only_transcript'][0]
# %%
real_data['topics'][43]