import streamlit as st

# Membaca file HTML dengan pivot table JavaScript
with open("files/pivottablejs (1).html", "r") as file:
    pivottable_html_content = file.read()
 
with open("files/folium_maps.html", "r") as file:
    folium_html_content = file.read()

# Display title for PivotTable
st.markdown("# PivotTable")
# Display PivotTable
st.components.v1.html(pivottable_html_content, height=400, width=2000, scrolling=True)

# Display title for Folium map
st.markdown("# Folium Map")
# Display Folium map
st.components.v1.html(folium_html_content, height=500, width=800, scrolling=True)   
