import streamlit as st
import streamlit.components.v1 as stc
import pandas as pd
import pygwalker as pyg

# Function for loading the CSV file
def load_data(data):
    return pd.read_csv(data)

def main():
    st.title("Streamlit PYGWALKER APP")

    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        with st.form("upload_form"):
            data_file = st.file_uploader("Upload a CSV file", ["csv", "txt"])
            submitted = st.form_submit_button("Submit")

            if submitted:
                df = load_data(data_file)
                st.dataframe(df)

                # Visualization
                pyg_html = pyg.walk(df, return_html=True)

                # Render with components
                stc.html(pyg_html, scrolling=True, height=1000)
    else:
        st.subheader("About")
        # Add information about your app or any other content for the "About" section

if __name__ == "__main__":
    main()
