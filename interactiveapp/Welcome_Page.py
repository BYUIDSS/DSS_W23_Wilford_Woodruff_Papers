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
    st.write("Our project uses a Graph Neural Network, or GNN, to analyze the Zinc database and identify potential drug candidates. The Zinc database is a large collection of purchasable compounds that can be used for drug discovery. Traditional methods for identifying potential drug candidates from this database don't work well, though, because the compounds are represented as nodes in a graph with various relationships represented as edges in the graph, such as similarity or chemical properties. By using a GNN and leveraging the graph structure of the database, we aim to overcome these limitations and discover new drugs that could save lives.")
    st.write("To overcome these challenges, we can use a GNN to learn representations of the compounds that take into account their relationships with each other. This allows us to identify potential drug candidates that may have been missed by traditional methods.")
    # st.write("## What we are trying to solve")


welcome_page()
