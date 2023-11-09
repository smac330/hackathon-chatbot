import streamlit as st

def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.write("# Welcome to Streamlit! 👋")

    st.markdown(
      """
       Welcome to the page!
      """
    )


if __name__ == "__main__":
    run()
