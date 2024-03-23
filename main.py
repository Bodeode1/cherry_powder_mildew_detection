import streamlit as st
from app_pages import single_image, multiple_images, about, image_gallery,performance

st.set_page_config(page_title="Cherry Leaf Disease Detection", layout="centered")
st.sidebar.title('Navigation')
page = st.sidebar.radio('Go to', ['Single Image Prediction', 'Multiple Images Prediction', 'Image Gallery Prediction', 'About Page','Model Performance Page'])

if page == 'Single Image Prediction':
    single_image.show()
elif page == 'Multiple Images Prediction':
    multiple_images.show()
elif page == 'Image Gallery Prediction':
    image_gallery.show()
elif page == 'About Page':
    about.show()
elif page == 'Model Performance Page':
    performance.show()
