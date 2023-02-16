import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

def code_page():
    '''
    Goals:
    1. Show the code of how we solved each topic
    2. Explain what this page is for
    '''
    st.title("Code")

    def get_started():
        st.header("Welcome")

    def topic1():
        st.header("Date Column")

    def topic2():
        st.header("Location")

    def topic3():
        st.header("Scripture")

    def topic4():
        st.header("Topics")
    

        st.markdown('##### The code begins by defining a list of specific religious topics. It then reads a CSV file, "wwp.csv", into a pandas dataframe named "wwp", and renames one of the columns to "text_only_transcript".')
        st.text("Import the required libraries")
        
        st.code("""
import pandas as pd
import altair as alt
import numpy as np
        ""","Python")


        st.text("Define a list of topics to be used for filtering the dataset")
        topics_list = ['repent', 'Family', 'Conference', 'Help', 'Death', 'Fish', 'Apostle', 'Jesus', 'God', 
                   'Holy Ghost', 'Priesthood', 'Women', 'Agency', 'Accountability', 'Depression', 'Encouragement', 
                   'Hope', 'Mercy', 'Sorrow', 'Baptism', 'Bible', 'Blessings', 'Brotherhood', 'Sisterhood', 
                   'Kingdom', 'Charity', 'Chastity', 'Christmas', 'Commandments', 'Commitment', 'Compassion', 
                   'Consecration', 'Courage', 'Creation', 'Diligence', 'Discouragement', 'Duty', 'Enduring', 
                   'Eternal', 'Life', 'Exaltation', 'Example', 'Fatherhood', 'Forgiveness', 'Gathering', 'Israel', 
                   'Temple', 'Temple Work', 'Goals', 'Grace', 'Gospel', 'Gratitude', 'Guidance', 'Home']
        st.code(f"topics_list = {topics_list}", "python")


        st.text("Read in the original dataset and rename the relevant column")
        wwp = pd.read_csv("./notebook/wwp.csv")
        wwp.rename(columns={"Text Only Transcript": "text_only_transcript"}, inplace=True)
        st.code("""
wwp = pd.read_csv("./notebook/wwp.csv")
wwp.rename(columns={"Text Only Transcript": "text_only_transcript"}, inplace=True)
        ""","Python")

        st.markdown('##### The next step is to clean the data in the dataframe by replacing missing or invalid values with empty strings, and replacing the HTML entity "&" with the word "and".')
        st.text("""Clean the dataset by removing empty values and replacing certain characters
        with their corresponding strings""")
        clean = (wwp
                .replace([-999, "", "NAN", "nan", "n/a", "NaN", np.nan], "")
                .replace("&amp;", "and"))

        st.code("""clean = (wwp
                .replace([-999, "", "NAN", "nan", "n/a", "NaN", np.nan], "")
                .replace("&amp;", "and"))""","Python")


        st.markdown('##### An empty list is then added to a new column called "topics" for each row in the dataframe, using a list comprehension.')
        st.text("Add an empty list in a new column called \"topics\" for each row in the cleaned dataset")
        clean['topics'] = [[] for _ in range(len(clean))]
        st.code("clean['topics'] = [[] for _ in range(len(clean))]", "Python")


        st.markdown('##### Next, the code defines a function, "filter_my_data", which takes a pandas dataframe and a search string as arguments, and returns a filtered dataframe that contains only the rows in which the "text_only_transcript" column contains the search string.')
        st.text("Define a function to filter data based on a specific string")
        def filter_my_data(pd_dataframe, filter_exp):
            return pd_dataframe.query('text_only_transcript.str.contains(@filter_exp)')
        st.code("""
def filter_my_data(pd_dataframe, filter_exp):
    return pd_dataframe.query('text_only_transcript.str.contains(@filter_exp)')
        ""","Python")


        st.markdown('##### The function "findPlace_topics" takes the cleaned dataframe, and one of the topics from the topics list as arguments, and uses the "filter_my_data" function to filter the dataframe by the topic. The rows in the filtered dataframe are then iterated over, and the current topic is added to the "topics" list for each row.')
        st.text("Define a function to extract relevant data for each word in the topics_list")
        def findPlace_topics(clean, topic):
            filtered_dataframe = filter_my_data(clean, topic)
            for index in filtered_dataframe.index:
                clean['topics'][index].append(topic)
            return filtered_dataframe, clean

        st.code("""
def findPlace_topics(clean, topic):
    filtered_dataframe = filter_my_data(clean, topic)
    for index in filtered_dataframe.index:
        clean['topics'][index].append(topic)
    return filtered_dataframe, clean
        ""","Python")


        st.markdown('##### The "findPlace_topics" function is then called for each topic in the topics list, resulting in the "topics" column for each row containing a list of all the topics that appear in the corresponding transcript.')
        st.text("Loop over each word in the topics_list and extract relevant data for each word")
        for i in topics_list:
            filtered_dataframe, clean = findPlace_topics(clean, i)

        st.code("""
for i in topics_list:
    filtered_dataframe, clean = findPlace_topics(clean, i)
        ""","Python")

        
        st.text("Print out the first 5 rows of the extracted data")
        st.dataframe(filtered_dataframe.head(5))

        st.text("Print out the topics for a specific row")
        st.write(clean["topics"][154])

        st.text("Print out the first 10 rows of the cleaned dataset")
        st.dataframe(clean.head(10))

        st.markdown('##### Finally, the cleaned dataframe is saved to a new CSV file, "cleaned_wwp.csv".')
        st.text("Save the cleaned dataset to a CSV file")
        clean.to_csv(".\\notebook\\cleaned_wwp.csv")
        st.code("clean.to_csv(\".\\notebook\\cleaned_wwp.csv\")","Python")

        st.subheader("Summary")
        st.text('''
        In summary, the code snippet provided performs a series of data cleaning and 
        transformation steps on a dataset of religious transcripts, ultimately resulting 
        in a new column in the dataset that contains lists of topics related to the 
        religious content in each transcript. Specifically, the code reads in a 
        CSV file of transcripts from the Wilford Woodruff Papers, which are primary 
        sources related to the history of the Church of Jesus Christ of Latter-day Saints,
        and renames one of the columns to make it easier to work with. It then cleans 
        the data, replacing various types of missing or invalid data with empty strings, 
        and creates a new column in the dataset that will be used to store the religious 
        topics for each transcript.

        To populate this new column with the appropriate topics for each transcript, 
        the code loops through a predefined list of religious topics and uses regular 
        expressions to identify which transcripts contain each topic. For each topic, 
        the code first filters the dataset to only include transcripts that contain 
        that topic, and then adds the topic to the list of topics associated with each 
        relevant transcript in the new column. By doing this for all of the topics 
        in the list, the code ultimately creates a new dataset with additional 
        information about the religious topics present in each transcript.

        The resulting dataset can be used for a variety of purposes, such as 
        identifying common themes or patterns in the religious content of the 
        transcripts. This could be useful for researchers studying the history or 
        theology of the Church of Jesus Christ of Latter-day Saints, or for those 
        interested in examining the ways in which religion is discussed or portrayed 
        in primary source materials. By identifying the topics that are most commonly 
        discussed in the transcripts, researchers may be able to gain a deeper 
        understanding of the beliefs, values, and practices of the people involved in 
        the historical events represented in the Wilford Woodruff Papers.Overall, this 
        code performs a useful preprocessing step for the Wilford Woodruff Papers 
        dataset, allowing researchers to extract additional information from the 
        transcripts beyond the text itself. The resulting dataset can be used in a 
        variety of ways to gain insights into the religious content and themes present 
        in the transcripts, potentially leading to new discoveries and understandings 
        about the history and theology of the Church of Jesus Christ of Latter-day Saints.''')
    

    with st.sidebar:
        option = st.selectbox(
        'subpage',
        ('Welcome','Date','Location', 'Scripture','Topic'))

    if option == 'Welcome':
        get_started()
    elif option == 'Location':
        topic2()
    elif option == 'Date':
        topic1()
    elif option == 'Topic':
        topic4()
    elif option == 'Scripture':
        topic3()