import streamlit as st
class Kaggle:
    def __init__(self,url:str):
        st.write("### Kaggle Notebook")

        # Showing kaggle badge
        kaggle_url = f'<a href="{url}" target="_blank"><img align="left" alt="Kaggle" title="Open in Kaggle" src="https://kaggle.com/static/images/open-in-kaggle.svg"></a>'
        st.write("**URL**")
        st.code(kaggle_url)
        st.markdown(kaggle_url, unsafe_allow_html=True)