import pandas as pd
import streamlit as st
# import os
# from app.Utils.colors import class_to_colour
# from app.Utils.colors import class_to_colour_2
from app.Utils.Special_image import Show_Special_Image
from app.Utils.Special_Stats import Show_Special_Stats
# load data
df = pd.read_csv("../data/weapons_details.csv")

Specials = df['Special'].unique()

selected_Special = st.selectbox("Select a Special:", Specials)
selected_Special_data = df[df['Special'] == selected_Special]

Special_img = selected_Special_data['Special_Img'].iloc[0]
num_weapons = len(selected_Special_data)

# call function to return a colour based on weapon Special
block_colour = "#71D8B0"
block_colour_2 = "#3F3CB6"
st.divider()
st.markdown(f"<h1 style='text-align: center;'>{selected_Special}</h1>",
            unsafe_allow_html=True)


w_special = selected_Special_data['Special'].iloc[0]

Show_Special_Image(Special_img)


# Styling for the block
block_style = (
    f"display: inline-block; width: 100%; padding: 25px; border-radius: 8px; "
    f"background-color: {block_colour}; text-align: center;"
)

# Full-width block within a container
with st.container():
    bold_text = (
        "<p style='font-size: 24px; margin: 0;"
        "color:#ffffff; font-weight: bold;'>"
        "Number of weapons that use this Special:</p>"
    )
    normal_text = (
        f"<p style='font-size: 24px; margin: 0; color: #ffffff;'>"
        f"{num_weapons}</p>"
    )
    st.markdown(
        f"<div style='{block_style}'>{bold_text}{normal_text}</div>",
        unsafe_allow_html=True
    )

Show_Special_Stats(selected_Special, block_colour, block_colour_2)
