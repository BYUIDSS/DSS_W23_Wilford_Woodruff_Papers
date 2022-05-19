# %%
import re
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer

# %%
with open('derived_data/journals.txt') as journals_file:
    text = journals_file.read()

text = "I like the Lord, he is my lord."

word = "Lord"
count = len(re.findall("lord"))
print(count)