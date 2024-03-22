import pandas as pd
import streamlit as st
from src import model_utils
import altair as alt
from src.multiple_images_styles import set_multiple_images_style

def show():
    set_multiple_images_style()
    st.title("🍒 Cherry Leaf Disease Detection - Multiple Images")
    st.markdown("<h3 style='text-align: center;'>Download the dataset <a href='https://www.kaggle.com/datasets/codeinstitute/cherry-leaves' target='_blank'>here</a></h3>", unsafe_allow_html=True)

    uploaded_files = st.file_uploader("Upload cherry leaf images", type=["png", "jpg", "jpeg"],
                                      accept_multiple_files=True)

    if uploaded_files:
        cols = st.beta_columns(3)
        predictions = []

        if 'predictions' not in st.session_state:
            st.session_state.predictions = []

        if st.button('Predict All'):
            with st.spinner('Predicting...'):
                predictions = [model_utils.predict(file) for file in uploaded_files]
                st.session_state.predictions = predictions

        col_index = 0
        for idx, uploaded_file in enumerate(uploaded_files):
            col = cols[col_index % 3]
            with col:
                st.image(uploaded_file, use_column_width=True)
                if st.session_state.predictions:
                    # Display prediction result under each image
                    prediction_text = "Healthy" if st.session_state.predictions[idx] == 0 else "Powdery Mildew"
                    st.markdown(f'<div class="prediction-text">{prediction_text}</div>', unsafe_allow_html=True)
            col_index += 1

        if predictions:
            healthy_count = st.session_state.predictions.count(0)
            mildew_count = st.session_state.predictions.count(1)
            st.markdown(f"""
                                    <div style="font-size: 20px; font-weight: bold; color: #4CAF50; text-align: center;">
                                        Healthy: {healthy_count}, Powdery Mildew: {mildew_count}
                                    </div>
                                    """, unsafe_allow_html=True)

            data = pd.DataFrame({
                'Condition': ['Healthy', 'Powdery Mildew'],
                'Count': [healthy_count, mildew_count]
            })

            chart = alt.Chart(data).mark_bar().encode(
                x='Condition', y='Count', color='Condition'
            )
            st.altair_chart(chart, use_container_width=True)
