# %%
import re
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
import seaborn as sns

# %%
with open('derived_data/journals.txt') as journals_file:
    text = journals_file.read()

# %%
pattern = r"[A-Z]\w+\s\d+,\s\d{4}\s~\s[A-Z]\w+"

headers = re.findall(pattern, text)

dates = []
for header in headers:
    date = header.split('~')[0].strip()
    dates.append(date)

entries = re.split(pattern, text)
entries.pop(0) # removes summary

# %%
wwp_dict = {
    'date': dates, 
    'entry': entries
}
# %%
wwp = pd.DataFrame.from_dict(wwp_dict)

# %%
sia = SentimentIntensityAnalyzer()
wwp['sentiment'] = wwp['entry'].astype(str).map(sia.polarity_scores).str['compound']

# %%
wwp.to_csv('journal_sentiments.csv', index=False)
# %%
