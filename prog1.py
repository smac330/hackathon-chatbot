import streamlit as st

def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
        )

    st.write("# Welcome to Streamlit! 👋")

    st.markdown(
      """
       Welcome to the VSU ChatBot, Yappers! Yappers is here to help you with your classes and give encouragement to every student. Please enter a question in the chat box below!
      """
    )


if __name__ == "__main__":
    run()
