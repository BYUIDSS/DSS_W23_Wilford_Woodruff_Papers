'''
Description:
    - Creates txt file for each document type found in raw csv file
    - Appends text-only transcripts to corresponding txt files
'''

import pandas as pd

# load data
url = "wwp.csv"
wwp = pd.read_csv(url, encoding = 'unicode_escape')

DOC_TYPE_INDEX = 1
TEXT_INDEX = 9

# iterate through dataframe
for index, row in wwp.iterrows():

    # get document type and text-only transcript
    doc_type = row[DOC_TYPE_INDEX]
    text = row[TEXT_INDEX]

    # write to file
    with open(f"{doc_type.lower()}.txt", 'a', encoding = 'utf-8') as txt_file:
        txt_file.write(str(text))