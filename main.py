import streamlit as st
from app_pages import single_image, multiple_images, about

st.set_page_config(page_title="Cherry Leaf Disease Detection", layout="wide")
st.sidebar.title('Navigation')
page = st.sidebar.radio('Go to', ['Single Image Prediction', 'Multiple Images Prediction', 'About'])

if page == 'Single Image Prediction':
    single_image.show()
elif page == 'Multiple Images Prediction':
    multiple_images.show()
elif page == 'About':
    about.show()
