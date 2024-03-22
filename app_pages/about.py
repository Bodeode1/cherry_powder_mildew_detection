import streamlit as st

def show():
    st.title("About Powdery Mildew")

    st.markdown("""
            ## 🌿 Powdery Mildew in Cherry Plants
            Powdery mildew is a common fungal disease that affects a wide variety of plants. It appears as white or gray powdery spots on the leaves and stems of plants. 🍃 So, Effective treatment involves the use of fungicides and adopting proper gardening practices to prevent the spread of the disease. 🌱
     """)

    st.image('images/mildew.png', caption='Powdery Mildew on Cherry Leaves', use_column_width=True)

   st.markdown("""
           ## Project Overview

           - **Data Acquisition**: The cherry leaves dataset, comprising images categorized into healthy and powdery mildew-infected leaves, was fetched from Kaggle.

           - **Data Preparation**: Employed image preprocessing and augmentation techniques, such as rotation, shifting, and flipping, to enhance model training.

           - **Exploratory Data Analysis**: Conducted visualizations to understand the dataset's class distribution and the average color distribution among classes.

           - **Model Development**: Developed a CNN model, tuned its hyperparameters, and evaluated its performance using metrics such as accuracy, precision, and recall.

           - **Model Deployment**: The trained model was saved and integrated into this web application for real-time disease detection.
       """)
    st.markdown("""
           ## Hypotheses and Validation

           - **Hypothesis 1**: The machine learning model can accurately detect powdery mildew in cherry leaves through image analysis.

             **Validation**: The model's performance was evaluated using precision, recall, and F1-score on a designated test dataset. The validation criterion was set at a minimum accuracy of 90%.

           - **Hypothesis 2**: Identification of powdery mildew can be enhanced by analyzing the color and textural characteristics of cherry leaves.

             **Validation**: Utilized visualization plots to examine the primary color distributions and textural features that the model relies on for making predictions.
       """)

 st.markdown("""
           

           ## Model Archietecture
       """)
    st.image('images/diagram.png', caption='Model Architecture', use_column_width=True)
