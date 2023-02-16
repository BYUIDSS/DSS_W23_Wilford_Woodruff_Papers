import streamlit as st

def welcome_page():
    '''
    Goals:
    1. Introduce the problems
    2. Explain how we are going to solve the problems
    3. Introduce the tools we use for these problems
    '''
    st.title("Welcome Page")

    def welcome():
        st.header("Welcome")

        st.subheader("Introduction")
        st.write("""This is the welcome page for the Wilford Woodruff Journal Entries project. 
        Here, we will introduce the problems we are tackling, explain how we are going to solve 
        them, and introduce the tools we use for these problems.""")

        st.subheader("Goals")
        st.write("""Our goals for this project are:""")
        st.write("""1. Get the date column for all journal entries.""")
        st.write("""2. Get the location column for all journal entries and find their latitudes and longitudes.""")
        st.write("""3. Match scripture references in the journal entries.""")
        st.write("""4. Match journal entries to specific topics.""")

    def intro_prob():
        st.header("Problems")

        st.subheader("Task 1: Date Column")
        st.write("""The first task is to populate the date column with the dates for all possible entries. 
        Since the dates are not provided in the journal entries, we need to extract them from the entries using 
        regular expressions. Once we have the dates, we will create a new column in the data frame and populate it 
        with the extracted dates.""")
        #Code example goes here

        st.subheader("Task 2: Location Column")
        st.write("""The second task is to get the location column for all journal entries and find their latitudes 
        and longitudes. The location data is not available in the journal entries, so we need to use external APIs 
        to extract the location information. We will use the Google Maps Geocoding API to find the latitude and 
        longitude of each location mentioned in the journal entries. Once we have the latitude and longitude 
        information, we will create new columns in the data frame and populate them with the extracted location 
        information.""")
        #Code example goes here

        st.subheader("Task 3: Scriptures")
        st.write("""The third task is to match journal entries to specific scriptures. We will use natural language 
                    processing techniques to match journal entries to specific topics. We may use pre-trained models like 
                    BERT and GPT-3 to extract topics from the journal entries. Once we have the scriptures, we will create a new 
                    column in the data frame and populate it with the extracted topics.""")
        #example code here

        st.subheader("Task 4: Topic Matching")
        st.write("""The fourth task is to topic matching for each journal entry. We will use regular 
                    expressions to identify the topic references in the journal entries. We will then create a new column in 
                    the data frame and populate it with the extracted topics.""")
        #example code here


    def tools():
        st.header("Tools")
            
        st.subheader("Tool 1: Python")
        st.write("""We will be using Python as our primary programming language for this project. 
        Python is a popular, high-level programming language known for its simplicity, readability, and vast libraries. 
        It provides a range of tools for data processing, machine learning, and visualization. Here is an example 
        of Python code to find the first 10 prime numbers:""")
        st.code("""
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def first_n_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

print(first_n_primes(10))
                """, language="python")

        st.subheader("Tool 2: Streamlit")
        st.write("""We will be using Streamlit to create interactive data visualizations and dashboards for this project. 
        Streamlit is an open-source app framework that makes it easy to build and deploy machine learning models, 
        data visualizations, and other interactive applications with minimal effort. It allows us to create interactive 
        visualizations and dashboards with just a few lines of Python code. Here's an example of a simple Streamlit app:""")
        st.code("""
import streamlit as st

st.title("My First Streamlit App")
st.write("Hello, world!")
                """, language="python")

        st.subheader("Tool 3: Regular Expressions")
        st.write("""We will be using regular expressions to match scripture references in the journal entries. 
        Regular expressions are a powerful tool for pattern matching and text processing. They allow us to search 
        for specific patterns in text data and extract relevant information. Here's an example of a regular expression 
        to match email addresses:""")
        st.code("""
                import re

email = "john.doe@example.com"
pattern = r"[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}"

if re.match(pattern, email):
    print("Valid email address")
else:
    print("Invalid email address")
                """, language="python")

        st.subheader("Tool 4: Natural Language Processing")
        st.write("""We will be using natural language processing techniques to match journal entries to specific topics. 
        Natural language processing (NLP) is a subfield of artificial intelligence that focuses on the interaction between 
        natural human language and computers. It allows us to extract meaning from text data and perform tasks such as 
        sentiment analysis, named entity recognition, and topic modeling. Here's an example of a simple NLP task using 
        the Natural Language Toolkit (NLTK) library in Python:""")
        st.code("""
                import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

text = "The quick brown fox jumps over the lazy dog"
tokens = word_tokenize(text)
filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]

print(filtered_tokens)
                """, language="python")

        st.subheader("Tool 5: Geocoding API")
        st.write("""We will be using a geocoding API to retrieve the latitude and longitude coordinates of locations mentioned 
    in the journal entries. Geocoding is the process of converting an address or place name into a set of geographic coordinates. 
    This allows us to visualize the location of the journal entries on a map and perform geospatial analysis. Here's an example 
    of how to use the Google Maps Geocoding API in Python to retrieve the latitude and longitude of a location:""")
        st.code("""
                import requests
address = "1600 Amphitheatre Parkway, Mountain View, CA"
params = {'address': address, 'key': 'YOUR_API_KEY'}
base_url = 'https://maps.googleapis.com/maps/api/geocode/json'

response = requests.get(base_url, params=params).json()
location = response['results'][0]['geometry']['location']
latitude = location['lat']
longitude = location['lng']

print(latitude, longitude)
""", language="python")

        st.subheader("Tool 6: Visualization Libraries")
        st.write("""We will be using various data visualization libraries to create interactive visualizations and 
        dashboards for the journal entries. These libraries allow us to create informative and engaging data visualizations 
        that help us to explore and communicate our insights effectively. Here are a few examples of popular data visualization 
        libraries in Python:""")
        st.write("""
        - Matplotlib: A powerful plotting library for creating static, animated, and interactive visualizations in Python.
        - Plotly: An interactive plotting library that allows us to create dynamic and interactive visualizations in Python.
        - Bokeh: A Python library for creating interactive data visualizations and dashboards in web browsers.
        - Seaborn: A Python library for creating informative and attractive statistical graphics.
        - Altair: A declarative visualization library for creating interactive visualizations in Python.
        """)


    with st.sidebar:
        option = st.selectbox(
        'subpage',
        ('Welcome','Problem','Tools'))

    if option == "Welcome":
        welcome()
    elif option == 'Problem':
        intro_prob()
    elif option == 'Tools':
        tools()