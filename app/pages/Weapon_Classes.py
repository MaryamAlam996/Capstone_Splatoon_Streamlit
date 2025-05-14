import pandas as pd
import streamlit as st
# import os
from app.Utils.colors import class_to_colour
from app.Utils.colors import class_to_colour_2
from app.Utils.Class_image import Show_Class_Image
from app.Utils.Class_stats import Show_Class_Stats

# load data
df = pd.read_csv("../data/weapons_details.csv")

weapon_classes = df['Class'].unique()

selected_class = st.selectbox("Select a class:", weapon_classes)
selected_class_data = df[df['Class'] == selected_class]

class_img = selected_class_data['Class_Img'].iloc[0]
num_weapons = len(selected_class_data)

# call function to return a colour based on weapon class
block_colour = class_to_colour(selected_class)
block_colour_2 = class_to_colour_2(selected_class)
st.divider()
st.markdown(f"<h1 style='text-align: center;'>{selected_class}</h1>",
            unsafe_allow_html=True)

# w_class = selected_class_data['Class'].iloc[0]
Show_Class_Image(class_img, selected_class)


# load the data
all_ability_stats_df = pd.read_csv("../data/Weapon_Class_ability_means.csv")
# Only get data of the chosen class
ability_stats_df = all_ability_stats_df[
    all_ability_stats_df['Class'] == selected_class
    ]
# count of the number of builds
Builds_count = ability_stats_df.iloc[0]
Builds_count = Builds_count.iloc[-1]



# Styling for the block
block_style = (
    f"display: inline-block; width: 100%; padding: 25px; border-radius: 8px; "
    f"background-color: {block_colour}; text-align: center;"
)

# Full-width block within a container
with st.container():
    bold_text = (
        "<p style='font-size: 24px; margin: 0; color: #ffffff; font-weight: bold;'>"
        "Number of weapons in this class:</p>"
    )
    normal_text = (
        f"<p style='font-size: 24px; margin: 0; color: #ffffff;'>"
        f"{num_weapons}</p>"
    )
    st.markdown(
        f"<div style='{block_style}'>{bold_text}{normal_text}</div>",
        unsafe_allow_html=True
    )

Show_Class_Stats(selected_class, block_colour, block_colour_2)


# st.dataframe(df)