import streamlit as st

def run():
    st.setPageConfig(
        pagetitle="VSU ChatBot",
        pageIcon="👋",
        )

    st.write("# Welcome to the VSU ChatBot, Yappers!👋")

    st.markdown(
      """
         Yappers is here to help you with your classes and give encouragement to every student. Please enter a question in the chat box below!
      """
    )

    question = st.textInput("Enter Question: " + "What's your major?")
    st.write("The question you asked was: " + question)


if __name__ == "__main__":
    run()
