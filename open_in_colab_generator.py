# streamlit run c:\Users\lenovo\Desktop\VSCode\stramlit.py

import streamlit as st
from src.is_colab import Colab
from src.is_kaggle import Kaggle
from src.is_binder import Binder
from src.is_livebook import LiveBook
from src.github_codespace import CodeSpace
from src.base import types

st.title("Open-in Badge Generator")
# st.container(overflow='hidden')

github_link = st.text_input('Github link: ','')
is_kaggle_notebook = st.checkbox("Is Kaggle Notebook", help="is this a link to a kaggle notebook?")

if not is_kaggle_notebook:
    link_splitted = github_link.split('/')
    branch , file_name = "main" , ""
    if github_link != "" and len(link_splitted) >= 6:
        # repo = "".join(link_splitted[3:5])
        branch = link_splitted[6]
        file_name = "/".join(link_splitted[7:])


    colab_link = github_link.replace("https:/","") # Removing https:/
    colab_link = colab_link.replace(".com","") # Remving .com

    binder_link = '/'.join(colab_link.replace("/github","").replace('/tree','').split('/')[1:3]) + "/" + branch

    codespace_link = '/'.join(colab_link.replace("/github","").replace('/tree','').split('/')[1:3])
    githubdev_link = github_link.replace('github.com','github.dev')

############
st.divider()
############

if not is_kaggle_notebook:
    Colab(colab_link)
    st.divider()
    Binder(binder_link, file_name=file_name)
    st.divider()
    CodeSpace(codespace_link,githubdev_link)
    st.divider()
    LiveBook(github_link)
else:
    Kaggle(github_link)
