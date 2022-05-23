# %%
import re
import pandas as pd

# %%
with open("../../derived_data/letters.txt", encoding = 'utf-8') as letters_file:

    text = letters_file.read()

# %%
name_pattern = r"\[\[.*\|.*\]\]" # NEEDS WORK

names = re.findall(name_pattern, text)

letters = re.split(name_pattern, text)
letters.pop(0)

# %%
letters_dict = {
    'names': names, 
    'letters': letters
}

letters_df = pd.DataFrame.from_dict(letters_dict)

# %%