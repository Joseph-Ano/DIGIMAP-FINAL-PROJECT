import streamlit as st
import math
from PIL import Image
from ditheringAlgorithm import *
from io import BytesIO

def main():
    errorExists = False
    st.title("DIGIMAP FINAL PROJECT")
    st.subheader("Floyd-Steinberg Dithering filter")

    image_file = st.file_uploader("Upload an image", ["jpeg", "jpg", "png"])
    sidebar = st.sidebar
    sidebar.header("S11 Group 1")
    sidebar.markdown('''**Members:**\n- Joseph Ano\n- Solomon Castillo\n- Jared Limjoco\n- Ramon Mapua''')

    nc_input = sidebar.text_input('''Enter number of colors for palette restriction\n(Example: Input of 8 = 2 bits per RGB channel)''')

    if(image_file):
        uploaded_image = Image.open(image_file)
        st.text("Uploaded Image")
        st.image(uploaded_image)

    filterBtn = st.button("Apply filter", key="filterBtn")
            
    if(filterBtn and not image_file):
        st.warning("Upload an image first")

    elif(filterBtn and image_file):
        try:
            nc_input = int(nc_input)
        except:
            st.warning("Input must be a positive number")
            errorExists = True
        
        if(errorExists == False and nc_input < 1 ):
            st.warning("Input must be a positive number")
            errorExists = True

        if(errorExists == False):
            nc_input = math.floor(nc_input**(1/3))

            img = dithering_algorithm(uploaded_image, nc_input)
            st.image(img)

            buf = BytesIO()
            img.save(buf, format="JPEG")
            byte_im = buf.getvalue()
            
            downloadBtn = st.download_button(label="Download Image", data=byte_im, file_name="ditheredImg.png", mime="image/jpeg")

if __name__ == "__main__":
    main()