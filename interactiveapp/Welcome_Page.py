import streamlit as st
import streamlit.components.v1 as components
import os
from PIL import Image
# from visual_displays.welcome import welcome_page
# from visual_displays.gnn import graph_neural_network
# from visual_displays.code import code_and_validation
# from visual_displays.demo import demonstration

# Sidebar Section
# st.sidebar.title("Zinc Molecular Weight")


def welcome_page():
    st.write("# Welcome To The Wilford Woodruff Papers")
    st.write("Wilford Woodruff was the fourth president of The Church of Jesus Christ of Latter-day Saints, known for his early leadership in the Church, missionary work, and involvement in the migration to Utah. He was baptized in 1833 and served as a missionary in several states and in England. Wilford Woodruff is also remembered for his practice and later abandonment of plural marriage, as well as for his role as a historian and record-keeper. Woodruff passed away in 1898.")
    st.write("Our goal was to analyze the provided text file of Wilford Woodruff journals and populate the column data into the date column. We scanned the text file for location, people, and places. Another goal we had was to match text references from the journals to the scriptures. All this data was then used to create an interactive map. This map shows where Woodruff was during important events in his life.")
    # st.write("## What we are trying to solve")


welcome_page()
