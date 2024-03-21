import streamlit as st
from src import model_utils
from src.gallery_image_styles import set_gallery_image_styles

def show_carousel(images):
    if 'carousel_index' not in st.session_state:
        st.session_state.carousel_index = 0

    current_image = images[st.session_state.carousel_index]

    col_image, = st.beta_columns([1])
    with col_image:
        st.image(current_image, width=600)

    col_next, = st.beta_columns([1])
    with col_next:
        if st.button("Next"):
            st.session_state.carousel_index = (st.session_state.carousel_index + 1) % len(images)

    col_predict, = st.beta_columns([1])
    with col_predict:
        if st.button("Predict"):
            predict_image(current_image)

def predict_image(image_path):
    prediction = model_utils.predict(image_path)
    prediction_text = "The leaf is healthy." if prediction == 0 else "The leaf has powdery mildew."
    st.markdown(f"<h1 style='text-align: center; color: red;'>{prediction_text}</h1>", unsafe_allow_html=True)

def show():
    st.title("🍒 Cherry Leaf Disease Detection - Gallery Prediction")
    set_gallery_image_styles()

    all_images = [
        'images/healthy/1.JPG', 'images/powder/2.JPG', 'images/healthy/3.JPG', 'images/powder/4.JPG',
        'images/healthy/5.JPG', 'images/powder/6.JPG', 'images/powder/1.JPG', 'images/powder/2.JPG',
        'images/powder/3.JPG', 'images/healthy/4.JPG', 'images/healthy/5.JPG', 'images/healthy/6.JPG'
    ]

    show_carousel(all_images)