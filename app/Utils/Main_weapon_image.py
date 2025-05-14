import streamlit as st
from PIL import Image
import requests
from io import BytesIO

from app.Utils.colors import class_to_big_splat
from app.Utils.colors import class_to_small_splat


# function to show the images related to each selected main weapon
def Show_Main_Images(main_img, sub_img, special_img, class_img, w_class):
    st.divider()
    # Create versions of each img with ink splat background
    M_img = Main_img(main_img, w_class)
    S_img = Sub_img(sub_img, w_class)
    SW_img = Special_img(special_img, w_class)
    # define columns and ratios (so we can place images)
    col_0, col_A, col_B = st.columns([1, 3, 3])
    # Main image is placed in col_A
    with col_A:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.image(M_img, width=400)

    # Sub and Special images in col_B
    with col_B:
        st.image(S_img, width=175)
        for i in range(5):
            st.write("")
        st.image(SW_img, width=175)
    return None


# --- Assistance from ChatGPT ------------------------------------------
# function that layers the main weapon img with the ink splat
def Main_img(main_img, w_class):
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


# function that layers the sub weapon img with the ink splat
# Same as Main_img function with small changes
def Sub_img(sub_img, w_class):
    # using small splats instead of big
    bg_img = "data/Small_Splats/" + class_to_small_splat(w_class)
    overlay = load_image_from_url(sub_img)
    background = Image.open(bg_img).convert("RGBA")
    scale = 0.4  # smaller overlay image
    new_size = (int(background.width * scale), int(background.height * scale))
    overlay_resized = overlay.resize(new_size)
    overlay_canvas = Image.new("RGBA", background.size, (0, 0, 0, 0))
    # set overlay to be at the center of the background
    # but slightly to the left and down
    offset = (((background.width - new_size[0]) // 2)-5,
              ((background.height - new_size[1]) // 2)+10)
    overlay_canvas.paste(overlay_resized, offset, mask=overlay_resized)
    # final image for the sub weapon
    composed_image = Image.alpha_composite(background, overlay_canvas)
    return composed_image


# function that layers the special weapon img with the ink splat
# Same as sub img function (defined if we want to change it later)
def Special_img(special_img, w_class):
    bg_img = "data/Small_Splats/" + class_to_small_splat(w_class)
    overlay = load_image_from_url(special_img)
    background = Image.open(bg_img).convert("RGBA")
    scale = 0.4
    new_size = (int(background.width * scale), int(background.height * scale))
    overlay_resized = overlay.resize(new_size)
    overlay_canvas = Image.new("RGBA", background.size, (0, 0, 0, 0))
    offset = (((background.width - new_size[0]) // 2)-5,
              ((background.height - new_size[1]) // 2)+10)
    overlay_canvas.paste(overlay_resized, offset, mask=overlay_resized)
    # final image for the special weapon
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
