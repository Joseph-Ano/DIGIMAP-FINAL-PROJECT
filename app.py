import streamlit as st
import pandas 
import cv2
import numpy as np
import os
from PIL import Image, ImageEnhance

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

            filter_type = st.sidebar.radio("Filters", ["Original", "Gray Scale", "Contrast"])

            if(filter_type == "Contrast"):
                rate = st.sidebar.slider("Contrast", 0.5, 6.0)

            if(st.button("Apply filter")):
                if(filter_type == "Gray Scale"):
                    img = np.array(uploaded_image.convert("RGB"))
                    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
                    st.image(gray)

                elif(filter_type == "Contrast"):
                    enhancer = ImageEnhance.Contrast(uploaded_image)
                    enhanced_img = enhancer.enhance(rate)
                    st.image(enhanced_img)
                    
if __name__ == "__main__":
    main()