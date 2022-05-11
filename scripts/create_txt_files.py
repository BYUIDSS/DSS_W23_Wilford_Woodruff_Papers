'''
Description:
    - Creates txt file for each document type found in raw csv file
    - Deletes previously derived data to avoid repeating text
    - Appends text-only transcripts to corresponding txt files
'''

import os
import pandas as pd
from bs4 import BeautifulSoup

# load data
file_path = "raw_data/wwp.csv"
wwp = pd.read_csv(file_path, encoding = 'unicode_escape')

DOC_TYPE_INDEX = 1
TRANSCRIPT_INDEX = 8

# erase previously derived data
for doc_type in wwp['Document Type'].unique():
    file_path = f"derived_data/{doc_type.lower()}.txt"
    if os.path.exists(file_path):
        os.remove(file_path)

# iterate through dataframe
for index, row in wwp.iterrows():

    # get document type and transcript
    doc_type = row[DOC_TYPE_INDEX]
    transcript = row[TRANSCRIPT_INDEX]

    # write to file
    file_path = f"derived_data/{doc_type.lower()}.txt"
    with open(file_path, 'a', encoding = 'utf-8') as txt_file:
        soup = BeautifulSoup(str(transcript), 'html.parser')
        txt_file.write(soup.get_text())