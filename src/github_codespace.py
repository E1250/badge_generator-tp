import streamlit as st

class CodeSpace:
    def __init__(self,codespace_url:str, githubdev_url:str):
        codespace_link = codespace_url
        githubdev_link = githubdev_url
        
        st.write("### Github Codespace")

        quickstart = "?quickstart=1" if st.checkbox(
            "Quick Start", help="Automatically create or reuse the most recent matching codespaces") else ""
        is_file = st.checkbox("Is File", help="Is it File or Repository")

        codespace_markdown = f'[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)]({f"https://codespaces.new/{codespace_link}{quickstart}" if not is_file else githubdev_link})'
        codespace_html = f'''<a href={f'https://codespaces.new/{codespace_link}{quickstart}' if not is_file else githubdev_link}><img src='https://github.com/codespaces/badge.svg' alt='Open in GitHub Codespaces' style='max-width: 100%;'></a>'''

        # Showing Codes
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Markdown**")
            st.code(codespace_markdown)

        with col2:
            st.write("**HTML**")
            st.code(codespace_html)

        st.markdown(codespace_markdown)
    
    def _prepare_url(self,url:str):
        pass