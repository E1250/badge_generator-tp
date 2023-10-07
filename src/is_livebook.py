import streamlit as st
class LiveBook:
    def __init__(self,url:str):
        github_link = url
        
        st.write("### Livebook")
        option_color = st.selectbox("Select Color : " , options = ['blue' , 'black' , 'gray' , 'pink'] , format_func = lambda option: {'blue':'Blue', 'black':'Black' , 'gray':'Gray' , "pink":"Pink"}.get(option))

        livebook_markdown = f'[![Run in Livebook](https://livebook.dev/badge/v1/{option_color}.svg)](https://livebook.dev/run?url={github_link})'
        livebook_html = f"""
        <a href="https://livebook.dev/run?url={github_link}">
        <img src="https://livebook.dev/badge/v1/{option_color}.svg" alt="Run in Livebook" />
        </a>
        """

        st.write("""
                **Note**: Elixir files Only
                """)

        # Showing Codes
        col1 , col2 = st.columns(2)
        with col1:
            st.write("**Markdown**")
            st.code(livebook_markdown)
            
        with col2:
            st.write("**HTML**")
            st.code(livebook_html)

        st.markdown(livebook_markdown)
