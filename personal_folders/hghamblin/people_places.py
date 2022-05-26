# %%
import re
import pandas as pd

# %%
with open("../../derived_data/journals.txt", encoding = 'utf-8') as journals_file:

    text = journals_file.read()

# %%
pattern = r"\[\[.*\|.*\]\]" # "[[ text, text | text ]]"
matches = re.findall(pattern, text)

# splits matches and removes brackets
clean_text = [text.split('|')[0][2:] for text in matches]
raw_text   = [text.split('|')[1][:-2] for text in matches]

# %%
wwp_dict = {
    'pair': matches,
    'clean': clean_text, 
    'raw': raw_text
}

wwp_df = pd.DataFrame().from_dict(wwp_dict)
wwp_df['clean'].value_counts()

# %%
def get_type(name):

    if name.find(',') == -1: # comma not found
        return 'person'
    else:
        return 'place'

# %%
wwp_df['name_type'] = wwp_df['clean'].map(get_type)
wwp_df['name_type'].value_counts()

# %%
