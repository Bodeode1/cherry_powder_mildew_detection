import streamlit as st
from src import model_utils, styles

def show():
    styles.set_layout_style()
    st.title("🍒 Cherry Leaf Disease Detection - Multiple Images")
    uploaded_files = st.file_uploader("Upload cherry leaf images", type=["png", "jpg", "jpeg"], accept_multiple_files=True)

    if uploaded_files:
        cols = st.columns(3)
        predictions = []

        if 'predictions' not in st.session_state:
            st.session_state.predictions = []

        if st.button('Predict All'):
            predictions = [model_utils.predict(file) for file in uploaded_files]
            st.session_state.predictions = predictions

        for idx, uploaded_file in enumerate(uploaded_files):
            with cols[idx % 3]:
                st.image(uploaded_file, use_column_width=True)
                if st.session_state.predictions:
                    prediction_text = "Healthy" if st.session_state.predictions[idx] == 0 else "Powdery Mildew"
                    st.markdown(f'<div class="prediction-text">{prediction_text}</div>', unsafe_allow_html=True)
