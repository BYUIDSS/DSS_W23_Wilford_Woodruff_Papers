import streamlit as st

def visual_page():
    '''
    Goals:
    1. Showcase a map representation of our data
    2. Showcase over the years and location which topic was most/never used
    3. Showcase over the years and location which scripture was most/never used

    '''
    st.title("Visual page")

    def get_started():
        st.header("Getting Started")

    def _map():
        st.header("Map")

    def topic():
        st.header("Find topic")

    def scripture():
        st.header("Find Scipture")

    with st.sidebar:
        option = st.selectbox(
        'subpage',
        ('Welcome','Map', 'Topic','Scripture'))

    if option == 'Welcome':
        get_started()
    elif option == 'Map':
        _map()
    elif option == 'Topic':
        topic()
    elif option == 'Scripture':
        scripture()