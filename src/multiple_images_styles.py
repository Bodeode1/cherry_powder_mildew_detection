import streamlit as st

def set_multiple_images_style():

    st.markdown("""
        <style>
        .prediction-text {
            font-size: 20px;
            color: #FF4B4B;
            font-weight: bold;
            text-align: center;
        }
        .stButton>button {
            font-size: 20px;
            width: 200px;
            height: 50px;
            border: 2px solid #4CAF50;
            border-radius: 25px;
            margin: 10px 0;
            display: block;
            margin-left: auto;
            margin-right: auto;
        }
        /* Additional styles if required */
        </style>
        """, unsafe_allow_html=True)
