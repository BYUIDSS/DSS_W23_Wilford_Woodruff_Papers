# %%
import re
import pandas as pd

# %%
with open("../../derived_data/journals.txt") as journals_file:
    journals = journals_file.read()

print(journals[:10])

# %%
people = [
    'George Albert Smith', 
    'Brigham Young', 
    'Joseph Smith Jr.', 
    'Heber Chase Kimball', 
    'John Taylor']
num_mentions = []

for person in people:
    num_mentions.append(len(re.findall(person, journals)))
# %%
people_df = pd.DataFrame().from_dict({
    "Name": people, 
    "Mentions": num_mentions
})
# %%
