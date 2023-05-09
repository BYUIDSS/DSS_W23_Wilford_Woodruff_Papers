import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns

def data():
    df = pd.read_csv("derived_data/cleaned_wwp.csv")
    st.title("Wilford Woodruff's Journals Data")
    st.dataframe(df)

    st.write(df.dtypes)

    df['text'] = df['text'].astype(str)
    text = " ".join(df['text'].dropna().tolist())
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    st.subheader("**Word Cloud Chart**")
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    st.pyplot()
    st.write('This code generates a word cloud chart. The data used for the chart is stored in a dataframe (\'df\') and is in the \'text\' column. The code first converts the \'text\' column to a string, then combines all the text data into one string. The WordCloud library is then used to generate the chart with a white background, and the chart is displayed using the \'streamlit\' library. The resulting chart shows the most commonly used words in the text data in a visually appealing way.')

    st.subheader("**Scatterplot of Date vs. Text Length**")
    # convert date column to datetime format
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # create a new column with text length
    df['text_length'] = df['text'].str.len()

    # create a scatterplot
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(df['date'], df['text_length'])
    ax.set_xlabel('Date')
    ax.set_ylabel('Text Length')
    ax.set_title('Scatterplot of Date vs. Text Length')
    st.pyplot(fig)
    st.write('The scatterplot displays the relationship between date and text length in a dataset. The date column is converted to datetime format using the pandas to_datetime() function, and a new column named \'text_length\' is created to store the length of the text using the str.len() function.')
    st.write('By examining the scatterplot, we can determine if there\'s a pattern or trend between the date and text length. This pattern may suggest that text length varies over time or is influenced by some external factor. The plot can also reveal any outliers, clusters, or gaps in the data.')

    # Stacked chart 
    st.subheader('**Stacked Area Chart of Topics over Time**')
    # create a new column with topics as a list
    df['topics_list'] = df['topics'].str.strip('[]').str.split(',')

    # create a new dataframe with topic frequency by year
    topic_freq = pd.DataFrame({'year': pd.DatetimeIndex(df['date']).year})
    for topic in set(df['topics'].str.strip('[]').str.split(',').sum()):
        topic_freq[topic] = df['topics_list'].apply(lambda x: x.count(topic) if topic in x else 0)
    topic_freq = topic_freq.groupby('year').sum()

    # create a stacked area chart
    fig, ax = plt.subplots(figsize=(8, 6))
    topic_freq.plot(kind='area', stacked=True, ax=ax)
    ax.set_xlabel('Year')
    ax.set_ylabel('Frequency')
    ax.set_title('Stacked Area Chart of Topics over Time')
    st.pyplot(fig)
    st.write('The code generates a stacked area chart to display the frequency of topics over time. The data is prepared by creating a new column with topics as a list and then counting the occurrences of each topic by year. The resulting data is plotted using the \'area\' chart type, with areas stacked on top of each other. This visualization enables viewers to track how the frequency of each topic changes over time and its contribution to the overall trend.')

    # Heatmap of Topic Frequency by Month and Year
    st.subheader("**Heatmap of Topic Frequency by Month and Year**")
    df['month'] = pd.DatetimeIndex(df['date']).month
    df['year'] = pd.DatetimeIndex(df['date']).year
    fig, ax = plt.subplots()
    topic_freq_month = pd.pivot_table(df, values='text', index='year', columns='month', aggfunc=lambda x: len(x.unique()))
    sns.heatmap(topic_freq_month, cmap='Blues', fmt='g')
    plt.xlabel("Month")
    plt.ylabel("Year")
    plt.title("Heatmap of Topic Frequency by Month and Year")
    st.pyplot()
    st.write('This Python code block generates a heatmap to visualize the frequency of topics over time. It creates two new columns in a DataFrame, \'month\' and \'year\', which are used to create a pivot table showing the unique number of texts by month and year. The pivot table is used to create the heatmap with darker shades indicating higher frequencies. The plot is then displayed using st.pyplot().')




    # create a new dataframe with place frequency
    df = pd.read_csv("derived_data/cleaned_wwp.csv")
    place_freq = pd.DataFrame(df['places'].str.strip('[]').str.split(',').explode().str.strip())

    # create a new dataframe with the number of entries by place
    entries_by_place = place_freq.groupby('places').size().reset_index(name='count')

    # Create a new dataframe with the names and places columns
    name_place_df = df[['names', 'places']]

    # Drop rows with missing values
    name_place_df = name_place_df.dropna()

    # Split names and places into separate lists
    names = [name.strip() for name_list in name_place_df['names'].str.strip('[]').str.split(',') for name in name_list]
    places = [place.strip() for place_list in name_place_df['places'].str.strip('[]').str.split(',') for place in place_list]

    # Create a dictionary to count the frequency of each name-place combination
    name_place_dict = {}
    for i in range(len(names)):
        name_place_dict[(names[i], places[i])] = name_place_dict.get((names[i], places[i]), 0) + 1

    # Create a network graph using Plotly
    edges = []
    for i in range(len(names)):
        edges.append((names[i], places[i], name_place_dict[(names[i], places[i])]))
    edge_df = pd.DataFrame(edges, columns=['Source', 'Target', 'Weight'])
    fig = px.scatter(edge_df, x='Source', y='Target', size='Weight', color='Weight')
    fig.update_traces(marker=dict(line=dict(width=0.5, color='black')), selector=dict(mode='markers'))
    fig.update_layout(title='Network Graph of Names and Places',
                      xaxis=dict(showticklabels=True),
                      yaxis=dict(showticklabels=True),
                      hovermode='closest')
    st.plotly_chart(fig)

    st.write('''The code creates a network graph using Plotly to visualize the frequency of name-place 
                combinations extracted from a cleaned CSV file. The Source column represents the names, 
                the Target column represents the places, and the Weight column represents the frequency 
                of the name-place combination. The graph is customized using the px.scatter function with 
                the size and color parameters set to Weight to control the size and color of the markers 
                based on the frequency.''')
    
    st.write('''
    The main use case for this code is data visualization. By creating a network graph, it allows you 
    to easily see the relationships between names and places in the data set, and the frequency of those 
    relationships. This can be useful in a variety of contexts, such as analyzing Wilford Woodruff behavior 
    in journals, mapping out his social habits in a community, or analyzing the geographic distribution of a 
    where he was.
    ''')



    





    

data()