import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static

def stories():
    df = pd.read_csv("derived_data/woodruff_life_event.csv")
    # # Create a Folium map object
    m = folium.Map(location=[df['latitude'].mean(), df['longitude'].mean()], zoom_start=2,  tiles='stamenterrain')
    # Add markers to the map with clickable tooltips that show event information
    for index, row in df.iterrows():
        tooltip = f"{row['Title']} on {row['Date']}"
        popup = folium.Popup(f"\"{row['Text']}\"<br><br>{row['Date']}<br><br>{row['Location']}", max_width=300)
        folium.Marker(location=[row['latitude'], row['longitude']],
                    tooltip=tooltip,
                    popup=popup,
                    ).add_to(m)
    # Display the map using the st.map() function
    st.title("Wilford Woodruff's Major Life Events")
    folium_static(m)





stories()