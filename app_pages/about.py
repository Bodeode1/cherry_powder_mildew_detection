import streamlit as st

def show():
    st.title("About Powdery Mildew")

    st.markdown("""
            ## 🌿 Powdery Mildew in Cherry Plants
            Powdery mildew is a common fungal disease that affects a wide variety of plants. It appears as white or gray powdery spots on the leaves and stems of plants. 🍃
     """)

    st.image('images/mildew.png', caption='Powdery Mildew on Cherry Leaves', use_column_width=True)

    st.markdown("""
         Effective treatment involves the use of fungicides and proper gardening practices to prevent the spread of the disease. 🌱

            The model is designed to detect powdery mildew in cherry plants using images of the leaves. By leveraging deep learning techniques, it can accurately distinguish between healthy leaves 🍒 and those affected by the disease. 🍂

        """)

    st.image('images/diagram.png', caption='Model Architecture', use_column_width=True)
