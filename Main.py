import streamlit as st
from app import main  # Assuming your main app logic is in app.py as a function `main()`

# Streamlit automatically runs the app when executed
if __name__ == "__main__":
    st.set_page_config(page_title="News Reader App", layout="wide")
    main()
