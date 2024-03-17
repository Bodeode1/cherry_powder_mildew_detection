import streamlit as st
from src import model_utils
from src.single_image_styles import set_single_image_style

def show():
    set_single_image_style()
    st.title("🍒 Cherry Leaf Disease Detection - Single Image")
    uploaded_file = st.file_uploader("Upload a cherry leaf image", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        st.markdown('<div class="image-margin">', unsafe_allow_html=True)
        st.image(uploaded_file, caption='Uploaded Image', width=700)
        st.markdown('</div>', unsafe_allow_html=True)
        if st.button('Predict'):
            prediction = model_utils.predict(uploaded_file)
            prediction_text = "The leaf is healthy." if prediction == 0 else "The leaf has powdery mildew."
            st.markdown(f'<p class="big-font">{prediction_text}</p>', unsafe_allow_html=True)
