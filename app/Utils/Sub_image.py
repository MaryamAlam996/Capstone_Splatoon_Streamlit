import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# function to show the images related to each selected main weapon
def Show_Sub_Image(s_img):
    st.divider()
    # Create versions of each img with ink splat background
    C_img = Sub_img(s_img)
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.image(C_img , width=300)

    # st.image(C_img, width=300)
    st.markdown("<br>", unsafe_allow_html=True)
    return None


# --- Assistance from ChatGPT ------------------------------------------
# function that layers the main weapon img with the ink splat
def Sub_img(main_img):
    # find the right ink splat to use for the Sub
    bg_img = "data/Small_Splats/Brush_1.png"
    # loading url image as the overlay
    overlay = load_image_from_url(main_img)
    # opening the splat image
    background = Image.open(bg_img).convert("RGBA")
    scale = 0.4  # Set the scale of the overlay
    # match the overlay size with the background and scale
    new_size = (int(background.width * scale), int(background.height * scale))
    overlay_resized = overlay.resize(new_size)
    # make a transparent canvas of the size of the ink splat img
    overlay_canvas = Image.new("RGBA", background.size, (0, 0, 0, 0))
    # Align the overlay to be in the centre of the background
    offset = (((background.width - new_size[0]) // 2)-5,
              ((background.height - new_size[1]) // 2)+10)
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
