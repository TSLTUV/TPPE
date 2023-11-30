import streamlit as st
from PIL import Image
from PIL.ImageFilter import *

# Title
st.markdown("<h1 style= 'text-align: center;'>Image Editor</h1>", unsafe_allow_html= True)
st.markdown("----")

# Image uploader
img_holder= st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

# Variable Holder
info= st.empty()
size= st.empty()
mode= st.empty()
format= st.empty()

if img_holder:
    UploadImage= Image.open(img_holder)
    # Image Info
    info.markdown("<h2 style= 'text-align: center;'>Information</h2>", unsafe_allow_html= True)
    size.markdown(f"<h6>Size: {UploadImage.size}</h6>", unsafe_allow_html= True)
    mode.markdown(f"<h6>Mode: {UploadImage.mode}</h6>", unsafe_allow_html= True)
    format.markdown(f"<h6>Format: {UploadImage.format}</h6>", unsafe_allow_html= True)

    # Image Resizing
    st.markdown("<h2 style= 'text-align: center;'>Resizing</h2>", unsafe_allow_html= True)
    width= st.number_input("width", value= UploadImage.width)
    height= st.number_input("height", value= UploadImage.height)

    # Image Rotating
    st.markdown("<h2 style= 'text-align: center;'>Rotation</h2>", unsafe_allow_html= True)
    degree= st.number_input("Degree")

    # Image Filter
    st.markdown("<h2 style= 'text-align: center;'>Filters</h2>", unsafe_allow_html= True)
    filters= st.selectbox("Filters", options= ("None", "Blur", "Contour", "Detail", "Emboss", "Edge_Enhance", "Sharpen", "Smooth"))

    # Editing Functionality
    s_btn= st.button("Submit")
    if s_btn:
        _edited_img= UploadImage.resize((width, height)).rotate(degree)
        filtered= _edited_img

        # Adding Functioning Filter
        if filters != "None":
            if filters == "Blur":
                filtered= _edited_img.filter(BLUR)
            elif filters == "Contour":
                filtered= _edited_img.filter(CONTOUR)
            elif filters == "Detail":
                filtered= _edited_img.filter(DETAIL)
            elif filters == "Emboss":
                filtered= _edited_img.filter(EMBOSS)
            elif filters == "Edge_Enchance":
                filtered= _edited_img.filter(EDGE_ENHANCE)
            elif filters == "Sharpen":
                filtered= _edited_img.filter(SHARPEN)  
            else:
                filtered= _edited_img.filter(SMOOTH)       
        st.image(filtered)    