import pandas as pd
import altair as alt
import numpy as np

from IPython.display import Markdown
from IPython.display import display
from tabulate import tabulate


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



filtered_dataframe = filter_my_data(clean, 'repent')

for index in filtered_dataframe.index:
    clean['topics'][index].append('repent')


print(filtered_dataframe.head(5))
print(clean["topics"][154])



