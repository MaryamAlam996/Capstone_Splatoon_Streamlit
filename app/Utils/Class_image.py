import streamlit as st
from PIL import Image
import requests
from io import BytesIO

from app.Utils.colors import class_to_big_splat
from app.Utils.colors import class_to_small_splat


# function to show the images related to each selected main weapon
def Show_Class_Image(class_img, w_class):
    st.divider()
    # Create versions of each img with ink splat background
    C_img = Class_img(class_img, w_class)
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.image(C_img , width=300)

    # st.image(C_img, width=300)
    st.markdown("<br>", unsafe_allow_html=True)
    return None


# --- Assistance from ChatGPT ------------------------------------------
# function that layers the main weapon img with the ink splat
def Class_img(main_img, w_class):
    # find the right ink splat to use for the class
    bg_img = "data/Big_Splats/" + class_to_big_splat(w_class)
    # loading url image as the overlay
    overlay = load_image_from_url(main_img)
    # opening the splat image
    background = Image.open(bg_img).convert("RGBA")
    scale = 0.65  # Set the scale of the overlay
    # match the overlay size with the background and scale
    new_size = (int(background.width * scale), int(background.height * scale))
    overlay_resized = overlay.resize(new_size)
    # make a transparent canvas of the size of the ink splat img
    overlay_canvas = Image.new("RGBA", background.size, (0, 0, 0, 0))
    # Align the overlay to be in the centre of the background
    offset = ((background.width - new_size[0]) // 2,
              (background.height - new_size[1]) // 2)
    # place the overlay image onto the transparent canvas
    overlay_canvas.paste(overlay_resized, offset, mask=overlay_resized)
    # final image for the main weapon
    # composed of the overlay and background images
    composed_image = Image.alpha_composite(background, overlay_canvas)
    return composed_image


# Load a url image
def load_image_from_url(url):
    response = requests.get(url)
    # Check if the request was successful
    response.raise_for_status()
    # return the url image in this form
    # so we can use it with st.image
    return Image.open(BytesIO(response.content)).convert("RGBA")
# -------------------------------------------------------------------------------------------------------
