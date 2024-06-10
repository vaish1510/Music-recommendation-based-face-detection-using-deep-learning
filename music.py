import streamlit as st

lang = st.text_input("language")
singer = st.text_input("singer")

btn = st.button("Recommend me songs")
