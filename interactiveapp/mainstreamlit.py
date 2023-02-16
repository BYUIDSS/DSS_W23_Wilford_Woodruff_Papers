import streamlit as st
import sys
#Make sure your path is correct
sys.path.append("C:\\Users\\tyler\\societies\\datascience\\ww_papers\\DSS_W23_Wilford_Woodruff_Papers")
from interactiveapp.streamlit_pages.Code_Page import code_page
from interactiveapp.streamlit_pages.Help_Page import help_page
from interactiveapp.streamlit_pages.Visuals_Page import visual_page
from interactiveapp.streamlit_pages.Welcome_Page import welcome_page


def main():
    #Activate the main pages
    with st.sidebar:
        option = st.selectbox(
        'Page:',
        ('Welcome', 'Visuals','Code','Help'))

    if option.lower() == 'welcome':
        welcome_page()
    elif option.lower() == 'visuals':
        visual_page()
    elif option.lower() == 'code':
        code_page()
    elif option.lower() == 'help':
        help_page()



if __name__ == "__main__":
    main()