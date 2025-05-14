import pandas as pd
import streamlit as st
import os
from app.Utils.colors import class_to_colour

# load data
df = pd.read_csv("../data/weapons_details.csv")

weapon_names = df['Name'].unique()
selected_weapon = st.selectbox("Select a weapon:", weapon_names)
selected_weapon_data = df[df['Name'] == selected_weapon]

st.markdown(f"<h1 style='text-align: center;'>{selected_weapon}</h1>", unsafe_allow_html=True)

# find fields
w_class = selected_weapon_data['Class'].iloc[0]
w_sub = selected_weapon_data['Sub'].iloc[0]
w_special = selected_weapon_data['Special'].iloc[0]
w_sp = selected_weapon_data['Special_Points'].iloc[0]
main_img = selected_weapon_data['Weapon_Img'].iloc[0]
sub_img = selected_weapon_data['Sub_Img'].iloc[0]
special_img = selected_weapon_data['Special_Img'].iloc[0]
class_img = selected_weapon_data['Class_Img'].iloc[0]

# st.markdown(f"## {w_class}")
# call function to return a colour based on weapon class
block_colour = class_to_colour(w_class)



all_w = [w_class, w_sub, w_special, w_sp]
# Create columns
col1, col2, col3, col4 = st.columns(4)
cols = [col1, col2, col3, col4]
names = ['Weapon Class', 'Sub <br>Weapon','Special Weapon','Special Points']

for numb in range(0, 4):
    with cols[numb]:
        st.markdown(f"""
            <div style="display: inline-block; padding: 25px; border-radius: 8px; 
                        background-color: {block_colour}; text-align: center;">
                <p style="font-size: 24px; margin: 0; color: #ffffff; font-weight: bold;">{names[numb]}:</p>
                <p style="font-size: 24px; margin: 0; color: #ffffff;">{all_w[numb]}</p>
            </div>
        """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# col_A, col_B = st.columns([3, 4])
# with col_A:
#     st.image(main_img, caption=selected_weapon, use_container_width=True)

# with col_B:
#     st.write("")
#     st.image(sub_img, caption=w_sub, width=100)
#     st.write("")
#     st.image(special_img, caption=w_special, width=100)

# st.markdown("<br><br>", unsafe_allow_html=True)

col_0, col_A, col_B = st.columns([0.5, 4, 2])  # Adjust the column width ratio (3:4)

# Main image
with col_A:
    st.write("")
    st.write("")
    st.image(main_img, width=350)

# Sub and Special images
with col_B:
    st.write("")
    st.image(sub_img, width=125)
    for _ in range(9):
        st.write("")
    st.image(special_img, width=125)

st.markdown("<br><br>", unsafe_allow_html=True)


# chat cha cha --------------

import streamlit as st
from PIL import Image
import requests
from io import BytesIO

def load_image_from_url(url):
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful
    return Image.open(BytesIO(response.content)).convert("RGBA")

# Load the main image from the URL
overlay = load_image_from_url(main_img) 

# Load the local background image
background = Image.open("data/Big_splats/Shooter.png").convert("RGBA")

# Resize the overlay to make it slightly smaller (optional)
scale = 0.65
new_size = (int(background.width * scale), int(background.height * scale))
overlay_resized = overlay.resize(new_size)

# Create a transparent canvas with the same size as the background
overlay_canvas = Image.new("RGBA", background.size, (0, 0, 0, 0))

# Calculate the offset to center the overlay on the background
offset = ((background.width - new_size[0]) // 2, (background.height - new_size[1]) // 2)

# Paste the resized overlay onto the transparent canvas at the calculated offset
overlay_canvas.paste(overlay_resized, offset, mask=overlay_resized)

# Composite the overlay and background into one image
composed_image = Image.alpha_composite(background, overlay_canvas)

# Display the final composed image
st.image(composed_image, use_container_width=True)
