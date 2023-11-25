import streamlit as st

# Membaca file HTML dengan pivot table JavaScript
with open("files/pivottablejs.html", "r") as file:
    html_content = file.read()

# Menyematkan konten HTML di dalam aplikasi Streamlit
st.components.v1.html(html_content, height=500, width=1200, scrolling=True)
