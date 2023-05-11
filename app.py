import streamlit as st
from essential_generators import DocumentGenerator


def get_data():
    data = DocumentGenerator()
    return data.sentence()


def display_user_input(data):
    st.write(data)


def main():
    st.title("Display EEG Data Application")
    st.markdown(
        "A application that receive data from the EEG headband and display for the user")

    st.header("Collecting Data:")

    while True:
        data = get_data()

        display_user_input(data)


if __name__ == "__main__":
    main()
