import streamlit as st


def main():
    """Main function to run the Streamlit app."""
    st.set_page_config(
        page_title="Splatoon Builds",
        page_icon="🦑🐙",
        layout="wide"
    )
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url(
                "https://pbs.twimg.com/media/FI5VLWZWUAMa3Oo?format=jpg&name=4096x4096");
            background-size: cover;
            background-position: bottom;
            background-attachment: fixed;
            background-blend-mode: multiply;
            background-color: rgba(100, 100, 100, 0.5)
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    # URLs
    # https://pbs.twimg.com/media/FI5VHVcX0AMS0Kn?format=jpg&name=large
    # https://pbs.twimg.com/media/FI5VLWZWUAMa3Oo?format=jpg&name=4096x4096
    # Header and navigation button
    st.markdown(
        '<h1 style="font-size: 100px; text-align: center; color: #FFFFFF;">'
        'Splatoon 3 Build Analysis</h1>',
        unsafe_allow_html=True
    )
    if st.button("Main Weapons"):
        st.switch_page("pages/Main_Weapons.py")


if __name__ == "__main__":
    main()
