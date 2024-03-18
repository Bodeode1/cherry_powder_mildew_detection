# Cherry Leaf Disease Detection

The Project focus on creating a full stack application which uses machine learning capabiltiy to detect powdery mildew disease in cherry leaves. In this study, a Convolutional Neural Network (CNN) is employed to examine imgaes of cherry leaves with the objective of categorizing them into two distinct groups: healthy or diseased. The project's result is a user-friendly Streamlit application that offers immediate predictions to users.

# Dataset Content
This project utilizes a dataset comprised of cherry leaf images sourced from kaggle (https://www.kaggle.com/datasets/codeinstitute/cherry-leaves). The dataset is specifcally desigined to challenge the issue of detecting powdery mildew diease in cherry leaves. The dataset consists of 4208 imgaes of cherry leaves that have been classified into two categories: 'powdery_mildew' and 'healthy'. The images utilized in this study were obtained from Kaggle's Cherry Leaves Dataset. By leveraging this dataset in this project, we hope to demonstrate a practical application that uses machine learning in agriculture to help reduce the labor-intensive manual task of detecting and inspecting plants to a more automated level, resulting in an efficient and scalable solution.

## Business Requirements
Farmy & Foods is currently facing a significant problem in their cherry farms, which involves the detection of powdery mildew, a prevalent fungal infection affecting cherry leaves. The existing procedure entails the manual inspection of individual cherry trees by personnel, a laborious effort that often requires approximately more then 30 to 40 minutes per tree. Given the extensive quantity of trees distributed among multiple farms, this approach is both inefficient and not capable of being expanded.

During the manual procedure, labourers visually examining leaves and, upon detecting powdery mildew, administering a treatment to the impacted region. The current manual inspection and treatment process really time consumming and is unable to effectively accommodate the extensive plantation, hence posing a significant danger of disease transmission and probable agricultural yield reduction.

The company is in need of a resolution in the shape of a machine learning system that possesses the capability to analyse leaf photographs and promptly ascertain their state of health. It is anticipated that this system will:

* Optimise the process of determining the presence of powdery mildew on a cherry leaf, eliminating the need for laborious manual examination.
* Precisely predict the occurrence of the  disease on the foliage, enabling timely and focused intervention to mitigate its dissemination.

### Alignment with CRISP-DM
 * Business Understanding: The project inception was driven based on the need to create a machine learning based system to counter the limiation of munual detection of powdery mildew diease in cherry leaf for farmers. 

 * Data Understanding: A preliminary evaluation of the cherry leaves dataset indicated its capacity to build a machine learning model that can differentiate between healthy and powdery mildew-infected leaves using visual features.

 * Data Preparation: A thorough preprocessing procedure was conducted on the dataset in order to appropriately prepare the images for the machine learning model. To enchance the peformance of the model, many techniques were used to genelize the data which include image resizing, normalization, and augmentation. 

 * Modeling: Since it was a image based classifcation task,  Convolutional Neural Network (CNN) technique was used. The selection of the CNN architecture was selected due to its efficacy in image classification, specifically designed to distinguish between healthy and diseased cherry leaves.

 * Evaluation: The performance of the model was evaluated by assessing its accuracy, precision, recall, and F1-score, in addition to a confusion matrix. This evaluation showcased the reliability of the model in detecting diseases.

 * Deployment: A Streamlit application was created, give the option of uploading of leaf photos for immediate disease prediction, hence enhancing the accessibility of the technology for individuals without expertise in the field.

# Hypothesis and Validation

* **Hypothesis 1**: The machine learning model demonstrates a high level of accuracy in detecting powdery mildew in cherry leaves based on image analysis.
    * **Validation**: Assess the model's performance using evaluation metrics like precision, recall, f1-score on a designated test dataset to verify that it meets or surpasses a pre-established accuracy criterion, such as 90%. 

* **Hypothesis 2**: The identification of powdery mildew disease can be facilitated by examining the colour and textural characteristics of cherry leaves.
    * **Validation**: Employ visualisation plot to identify the primary color distribution and features upon which the model heavily relies for predicating outcomes.

#  Map Business requirements to the Data Visualisations and ML tasks
The primary objective of this research is to facilitate the effective and precise identification of powdery mildew in cherry leaves, with the aim of assisting farmers and agricultural experts in early detection of diease and and preveneting crop damages. 
The following user stories map certain machine learning and data visualizations task, outlining the actions needed for their implementation:

### User Story 1: Early Detection for Timely Intervention

* **As a** Cherry farmer,
* **I want** an automated tool to detect powdery mildew on cherry leaves accurately,
* **So that** I can use it for early detection and prevent the spread of the disease.
* ML Task: Development of Convolutional Neural Network Model for the classfication of cherry leaf as healthy or powdery mildew.
* Data visualization: Display each image prediction along with chart to show how many are healthy and powdery mildew on the Streamlit app to give a clear feedback on the model assessment.

### User Story 2: Understand Disease Prevalence

* ***As an*** agricultural specialist
* **I want** to have a system which can help in analyzing the prevalence of powdery mildew in multiple different crops of cherry.
* **So that** it can help in advicing farmers to implement different diease management strategies more effectively and timely.
* ML Task: Aggregate the overall predictions data to easily analyze diease across multiple iamges of different cherry crops and tell which crops have the issues.
* Data Visualization: implementation of Bar charts in the Streamlit app to show the proportion (Count) of healthy vs powdery mildew among the uploaded cherry crop images, helping in understanding how much the diease is spread in that specific crop.

### User Story 3: Insights Into Model Accuracy
* **As an** plant pathology researcher
* **I want** to understand the performance of the model to evaluate.
* **So that** I can help trust the tool for academic reasearch
* ML Task: Provide detail evaluation method which include acccuracy, precision ,recall, F1-score and confusion matrix.
* Data Visualization: Provide a compreshensive analysis section which contain proper plot of Confusion matrix and precision, recall, f1-score table.

## ML Business Case
The comprehensive insights that are crucial for corporate decision-making can be obtained through the analysis of visualizations and the interpretation of machine learning (ML) outcomes that are map according to busniess requirements. Following are the analytics and visulization outcome based on each business case. 

* **Class Distribution**: To ensure that data is distrbuted correctly and there is not class imbalance, we analyzed the distribution of healthy and powder mildew classes, using barplot. From the bar chart analysis, it was clear that the distribution of classes are evenly balanced, with a nearly equal number of images for both healthy and powdery mildew-infected cherry leaves. 
this balance show that data is not class imbalanced and model will be not baised toward a specific class.
![alt text](https://github.com/Bodeode1/cherry_powder_mildew_detection/blob/main/images/class.png?raw=true)

* **Average Color Distribution & Difference in Color Intensity**:
Histogram was created to show the visual representation of the average color distribution which offers  insights into the contrasting color characteristics between healthy leaves and leaves affected by powdery mildew. The chart shows the pixel intensity within three distinct color channels, namely Red, Green, and Blue, pertaining to the condition of cherry leaves. The curves illustrate the occurrence rate of various pixel intensity values. A higher peak height indicates a greater prevalence of a specific intensity within the sample. For healthy leaves, it looks like the peaks are at similar intensity values across all three color channels, suggesting a balanced color representation, though the distribution curves slightly differ from the healthy leaves, The red channel in this instance displays the biggest difference, followed by the green and blue channels. This suggests that the effects of powdery mildew on leaf color are particularly noticeable in the red channel hence indicating that the pixel denstiy of color changes due to the disease.

![alt text](https://github.com/Bodeode1/cherry_powder_mildew_detection/blob/main/images/average.png?raw=true)

* **Model Performance Metrics**: The classification report and confusion matrix provide a thorough analysis of the model's prediction power. 
from the charts we can see that model achieve an precision, recall, and F1-score values of 0.99 percent for both classe, which showed that CNN model did a very good job of accurately identifying the cherry leaves dieases.
![alt text](https://github.com/Bodeode1/cherry_powder_mildew_detection/blob/main/images/ac.png?raw=true)
![alt text](https://github.com/Bodeode1/cherry_powder_mildew_detection/blob/main/images/loss.png?raw=true)
![alt text](https://github.com/Bodeode1/cherry_powder_mildew_detection/blob/main/images/cr.png?raw=true)
![alt text](https://github.com/Bodeode1/cherry_powder_mildew_detection/blob/main/images/cm.png?raw=true)

* ## Main Data Analysis and Machine Learning Libraries

* **Python**: Main Langague we used to create the Application and Machine learning model
* **Streamlit**: Library used to create the Front End Application to detect Cherry leaf diease
* **TensorFlow/Keras**: Library used to create the machine learning model to train on images
* **keras_tuner**: Library used to apply hyperparemeter tunning on CNN model.
* **Pandas**: Library used for data manupilation in front end application
* **NumPy**: Library used to handle array and mumerical manupilation
* **cv2**: Library used to load imgs and plot them
* **Altair/Seaborn/Matplotlib for visualization**: Library used to plot charts (such as bar charts, evaluation charts has (confusion matrix, loss and accuracy line charts etc)), Altair was used in frontend app to show total count of normal and powder mildew bar chart count chart

## Dashboard Design
The Streamlit dashboard is designed to provide an interactive user experience with three main sections:

* **Single Image Prediction**:
  * An upload box where users can upload an image of a cherry leaf.
  * After uploading, the image is displayed on the screen.
  * A 'Predict' button that, when clicked, will show the model's prediction right below the image.
  * Predictions are color-coded for easy identification - green for healthy and red for powdery mildew.

![alt text](https://github.com/Bodeode1/cherry_powder_mildew_detection/blob/main/images/s1.png?raw=true)

* **Multiple Images Prediction**:
  * An upload box allowing multiple images to be uploaded simultaneously.
  * Uploaded images are displayed in a gallery format.
  * A 'Predict All' button to analyze all images at once.
  * Each image is annotated with a prediction below it, following the same color-coding as the single image prediction.
  * A summary bar chart visualizing the count of healthy vs. powdery mildew leaves, empowering users to gain quick insights into the health of multiple cherry leaves.

![alt text](https://github.com/Bodeode1/cherry_powder_mildew_detection/blob/main/images/s2.png?raw=true)

* **About**:
  * Detailed information about powdery mildew and its impact on cherry leaves.
  * Visual aids to help users recognize symptoms of the disease.
  * An overview of the model's architecture, explaining how the AI makes its predictions.

![alt text](https://github.com/Bodeode1/cherry_powder_mildew_detection/blob/main/images/s3.png?raw=true)

This interface ensures that both experts and non-experts can efficiently utilize the tool to assess the health of cherry leaves.

## Unfixed Bugs

### IndexError in Multiple Image Prediction

**Issue**: Upon uploading a new set of images for prediction after an initial set has already been processed, the application throws an `IndexError: list index out of range`. This error does not occur when making predictions on the first set of images or upon clicking the 'Predict' button again after the error.

**Current Behavior**: The application is designed to store predictions in the session state for persistence across reruns. However, when new images are uploaded, and the 'Predict All' button is pressed during mutli image prediction, there seems to be a mismatch in the indices, causing the application to attempt to access a prediction index that does not exist.

**Potential Cause**: The error may be due to the session state not being reset or updated correctly when new images are uploaded, leading to an inconsistent state between the images displayed and the predictions list.

**Steps to Reproduce**:
1. Upload a set of images on multi image tab and use the 'Predict All' button to generate predictions.
2. Without refreshing or resetting the session, upload a new set of images this will show the error.

**Workaround**: Users can avoid this error just by clicking on predict All button and it will predict it all images including new set of images.

**Resolution Status**: This bug is acknowledged but remains unfixed. 

**Note**: This issue does not affect the core functionality of the prediction set and can be reliably bypassed using the described workaround.

![alt text](https://github.com/Bodeode1/cherry_powder_mildew_detection/blob/main/images/Error.png?raw=true)

## Deployment
### Heroku

* The App live link is:https://cherry-leaves-app-4554e70202ef.herokuapp.com/

* Runtime.txt Python version is set to python version 3.9.16

* The project was deployed to Heroku using the following steps.

        1. Log in to Heroku
        2. Click New and Click Deploy New App
        3. Give App Name
        4. Click on Deploy Tab and On Deployment method chose GitHub
        5. Search Your github repo where code is present and once found connect it with Heroku
        6. Select the Github branch (Usually main branch) and click Deploy Branch
        7. In Requirements file use tensorflow-cpu to install it else the slug size will be above 500mb and deployment will fail
        8. Once the Deployment is finish click on Open App button to access the Application

## Credits 

* Dataset provided by [Kaggle Cherry Leaves Dataset](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves).
* Python libraries documentation and communities for technical reference.
* [Heroku Dev Center](https://devcenter.heroku.com/articles/python-support) for deployment guidelines.
* Special thanks to the online community forums and Stack Overflow for providing solutions to specific coding challenges encountered during the project.
* Visualization plots were inspired by tutorials found on Seaborn's and Matplotlib's documentation as well has online sources such as (https://medium.com/@sehjadkhoja0/title-exploring-and-analyzing-image-data-with-python-79a7f72f4d2b).
