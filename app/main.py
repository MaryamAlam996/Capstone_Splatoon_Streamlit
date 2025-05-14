import streamlit as st
from app.Utils.colors import Set_Background


# Start Streamlit app
def main():
    """Main function to run the Streamlit app."""
    st.set_page_config(
        page_title="Splatoon Builds",
        page_icon="🦑🐙",
        layout="wide"
    )

    # Call function to set the main page background
    Set_Background()

    # Title
    st.markdown('<br><br><br><br><br><br><br>',
                unsafe_allow_html=True)
    st.markdown(
        '<h1 style="font-size: 100px; text-align: center; color: #FFFFFF;">'
        'Splatoon 3 Build Analysis</h1>',
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()
