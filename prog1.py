import streamlit as st

def run():
    st.set_page_config(
        page_title="VSU ChatBot",
        page_icon="👋",
        )

    st.write("# Welcome to the VSU ChatBot, Yappers!! 👋")

    st.markdown(
      """
        Yappers is here to help you with your classes and give encouragement to every student. Please enter a question in the chat box below!
      """
    )


if __name__ == "__main__":
    run()
    
