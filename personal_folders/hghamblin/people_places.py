# %%
import re
import pandas as pd
import geopy
from geopy.geocoders import Nominatim

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
places_df = wwp_df.query("name_type == 'place'").head(50)
# %%
geolocator = Nominatim(user_agent="WWPapers")
def get_latitude(town):
    try:
        location = geolocator.geocode(town)
        return location.latitude
    except:
        return ""
def get_longitude(town):
    try:
        location = geolocator.geocode(town)
        return location.longitude
    except:
        return ""
places_df['Latitude'] = places_df['clean'].map(get_latitude)
places_df['Longitude'] = places_df['clean'].map(get_longitude)
# %%
coordinateplaces_df = places_df.query("Latitude != ''")
# %%
coordinateplaces_df.to_csv('fullplaces.csv')
# %%
