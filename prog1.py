import streamlit as st
import pandas as pd

[theme]
primaryColor="#0908F5"
backgroundColor="#F58C08"
secondaryBackgroundColor="#E9F1F0"
textColor="#0A0A0A"
font= "sans serif"

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
    
