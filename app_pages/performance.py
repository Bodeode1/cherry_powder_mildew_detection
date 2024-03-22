import streamlit as st
import pandas as pd

def show():
    st.title("Model Performance Overview")

    st.markdown("""
    ## Convolutional Neural Network Evaluation

    The model's performance is evaluated through various metrics, such as accuracy, precision, recall, and F1-score on the test data which contained sperated images not used during training model. These metrics provide insights into the model's ability to classify cherry leaves correctly.

    ### Performance Charts
    """)

    st.image('images/ModelPerformance.png', caption='CNN Model Performance Metrics', use_column_width=True)

    st.markdown("""
        Charts Show Model overall Training and Validation Loss and accuracy. From the chart we can clearly see that:
        
        - Loss decreases over time as the model learns from the training dataset. It's the error rate on the data that the model uses to adjust its weights.
        - For accuracy we can see that it increases over time as the model trains, it adjusts to perform better on this data.
        - Morever, Validation loss and accuracy also shows almost same pattern which shows that model is not overfitting.
        """)

    st.markdown("""
    ### Classification Report

    The classification report provides detailed metrics for each class, including precision, recall, and F1-score.

    """)

    data = {
        'Class': ['0.0', '1.0'],
        'Precision': [0.99, 0.98],
        'Recall': [0.98, 0.99],
        'F1-score': [0.99, 0.99],
        'Support': [209, 211]
    }
    classification_report_df = pd.DataFrame(data)

    st.table(classification_report_df)

    st.markdown("""
    **Accuracy**: 0.99  
    **Macro Avg**: 0.99  
    **Weighted Avg**: 0.99  

    These results indicate a high-performing model, with an overall accuracy of 99%, suggesting that the model is excellent at distinguishing between healthy and powdery mildew-infected cherry leaves.""")
    st.markdown("""
    ## Interpretation of the Confusion Matrix

    The confusion matrix illustrates the model's performance with true positive and true negative predictions. It highlights the instances where the model may confuse one class for another.

    - **True Positives (TP)**: Correctly predicted powdery mildew-infected leaves
    - **True Negatives (TN)**: Correctly predicted healthy leaves
    - **False Positives (FP)**: Healthy leaves incorrectly identified as powdery mildew
    - **False Negatives (FN)**: Powdery mildew leaves incorrectly identified as healthy

    With 205 true negatives and 209 true positives, the model shows a high true classification rate. The low number of false positives (4) and false negatives (2) signifies that the model rarely misclassifies the leaves, further indicating its reliability.
    """)
    st.image('images/cm.png', caption='CNN Model Performance Metrics', use_column_width=True)
