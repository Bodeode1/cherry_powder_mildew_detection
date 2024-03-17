import streamlit as st
from src import model_utils, styles

def show():
    styles.set_layout_style()
    st.title("🍒 Cherry Leaf Disease Detection - Single Image")
    uploaded_file = st.file_uploader("Upload a cherry leaf image", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption='Uploaded Image', width=700)
        if st.button('Predict'):
            prediction = model_utils.predict(uploaded_file)
            prediction_text = "The leaf is healthy." if prediction == 0 else "The leaf has powdery mildew."
            st.markdown(f'<p class="big-font">{prediction_text}</p>', unsafe_allow_html=True)
