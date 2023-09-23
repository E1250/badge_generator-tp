import streamlit as st
    
class Colab:
    def __init__(self,url:str):
        colab_link = self._prepare_url(url)
        
        st.write("### Google Colab")

        colab_markdown = f'[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com{colab_link})'
        colab_url = f'<a href="https://colab.research.google.com{colab_link}" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>'

        # Showing Code
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Markdown**")
            st.code(colab_markdown)

        with col2:
            st.write("**URL**")
            st.code(colab_url)

        st.markdown(colab_markdown)
        
    def _prepare_url(self , url:str):
        pass