import streamlit as st
import numpy as np
from PIL import Image, ImageEnhance
from ditheringAlgorithm import *

def main():
    st.title("DIGIMAP FINAL PROJECT")
    st.text("Image editing web application")

    actvities = ["About", "Filter"]
    choice = st.sidebar.selectbox("Select an activity", actvities)

    if(choice == "Filter"):
        st.subheader("Filter")
        image_file = st.file_uploader("Upload an image", ["jpeg", "jpg", "png"])

        if(image_file):
            uploaded_image = Image.open(image_file)
            st.text("Uploaded Image")
            st.image(uploaded_image)

            filter_type = st.sidebar.radio("Filters", ["Original", "Floyd-Steinberg Dithering"])

            if(filter_type == "Floyd-Steinberg Dithering"):
                nc_input = st.sidebar.text_input("New colors")

            if(st.button("Apply filter")):
                if(filter_type == "Floyd-Steinberg Dithering"):
                    img = dithering_algorithm(uploaded_image, int(nc_input))
                    st.image(img)
                    
if __name__ == "__main__":
    main()