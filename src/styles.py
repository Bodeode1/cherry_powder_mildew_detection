import streamlit as st


def set_layout_style():

    st.markdown("""
        <style>
        /* Main page styling */
        ..big-font {
            font-size:25px !important;
            font-weight: bold;
            color: #4CAF50;
            text-align: center;
            margin-left: 52px
        }
        .image-display {
            display: flex;
            justify-content: center;
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
            margin-left: 266px;
        }
        
        .prediction-text {
            font-size: 20px;
            color: #FF4B4B;
            font-weight: bold;
            text-align: center;
        }

        </style>
        """, unsafe_allow_html=True)
