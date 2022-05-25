# %%
import re
import pandas as pd

# %%
with open("../../derived_data/letters.txt", encoding = 'utf-8') as letters_file:

    text = letters_file.read()

# %%
pattern = r"\[\[.*\|.*\]\]"

names = re.findall(pattern, text)

letters = re.split(pattern, text)
letters.pop(0)

# %%
letters_dict = {
    'names': names, 
    'letters': letters
}

letters_df = pd.DataFrame.from_dict(letters_dict)

# %%