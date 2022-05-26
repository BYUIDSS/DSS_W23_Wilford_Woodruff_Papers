# %%
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer

# %%
url = "https://github.com/BYUIDSS/DSS_S22_Wilford_Woodruff_Papers/blob/master/raw_data/wwp.csv?raw=true"
wwp = pd.read_csv(url, encoding = 'unicode-escape')

# %%
import nltk
sia = SentimentIntensityAnalyzer()
wwp['Sentiment'] = wwp['Text Only Transcript'].astype(str).map(sia.polarity_scores).str['compound']

# %%

